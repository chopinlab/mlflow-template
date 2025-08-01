import mlflow
import mlflow.sklearn
import pandas as pd
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

def create_sample_data():
    """간단한 분류 데이터셋 생성"""
    X, y = make_classification(
        n_samples=1000,
        n_features=20,
        n_informative=10,
        n_redundant=5,
        n_classes=2,
        random_state=42
    )
    
    feature_names = [f'feature_{i}' for i in range(X.shape[1])]
    df = pd.DataFrame(X, columns=feature_names)
    df['target'] = y
    
    return df

def train_model(df, experiment_name="ml_experiment"):
    """모델 학습 및 MLflow 실험 추적"""
    
    # MLflow 실험 설정
    mlflow.set_experiment(experiment_name)
    
    with mlflow.start_run():
        # 데이터 전처리
        X = df.drop('target', axis=1)
        y = df['target']
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        
        # 스케일링
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        # 하이퍼파라미터 설정
        n_estimators = 100
        max_depth = 10
        min_samples_split = 5
        
        # 모델 학습
        model = RandomForestClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth,
            min_samples_split=min_samples_split,
            random_state=42
        )
        
        model.fit(X_train_scaled, y_train)
        
        # 예측 및 평가
        y_pred = model.predict(X_test_scaled)
        y_pred_proba = model.predict_proba(X_test_scaled)[:, 1]
        
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        
        # MLflow 로깅
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)
        mlflow.log_param("min_samples_split", min_samples_split)
        mlflow.log_param("train_samples", len(X_train))
        mlflow.log_param("test_samples", len(X_test))
        
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("precision", precision)
        mlflow.log_metric("recall", recall)
        mlflow.log_metric("f1_score", f1)
        
        # Feature importance 시각화
        feature_importance = pd.DataFrame({
            'feature': X.columns,
            'importance': model.feature_importances_
        }).sort_values('importance', ascending=False)
        
        plt.figure(figsize=(10, 6))
        sns.barplot(data=feature_importance.head(10), x='importance', y='feature')
        plt.title('Top 10 Feature Importance')
        plt.tight_layout()
        plt.savefig('feature_importance.png')
        mlflow.log_artifact('feature_importance.png')
        plt.close()
        
        # 모델 저장
        mlflow.sklearn.log_model(
            model, 
            "random_forest_model",
            registered_model_name="RandomForestClassifier"
        )
        
        # 전처리기도 함께 저장
        mlflow.sklearn.log_model(
            scaler,
            "scaler"
        )
        
        print(f"모델 학습 완료!")
        print(f"Accuracy: {accuracy:.4f}")
        print(f"Precision: {precision:.4f}")
        print(f"Recall: {recall:.4f}")
        print(f"F1-Score: {f1:.4f}")
        
        return model, scaler

def main():
    """메인 실행 함수"""
    print("MLflow 모델 학습 템플릿 시작...")
    
    # 데이터 생성
    print("1. 샘플 데이터 생성 중...")
    df = create_sample_data()
    print(f"데이터 생성 완료: {df.shape}")
    
    # 모델 학습
    print("2. 모델 학습 시작...")
    model, scaler = train_model(df)
    
    print("3. 학습 완료!")
    print("\nMLflow UI 실행 명령:")
    print("mlflow ui")
    print("브라우저에서 http://localhost:5000 접속하여 실험 결과를 확인하세요.")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
MLflow 자동 추적 - 코드에 추적 로직을 넣지 않는 방법
"""
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# MLflow 설정
mlflow.set_tracking_uri("http://localhost:8080")

def clean_train_model():
    """
    깔끔한 모델 훈련 - 추적 코드 없음!
    MLflow가 자동으로 모든 것을 추적
    """
    print("🧹 깔끔한 모델 훈련 (자동 추적)")
    
    # 데이터 준비
    X, y = make_classification(n_samples=500, n_features=10, n_informative=5, 
                               n_classes=2, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 모델 훈련 - 추적 코드 전혀 없음!
    model = RandomForestClassifier(n_estimators=50, max_depth=8, random_state=42)
    model.fit(X_train, y_train)
    
    # 평가
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"✅ 훈련 완료 - 정확도: {accuracy:.4f}")
    print("📊 MLflow가 자동으로 모든 것을 추적했습니다!")
    
    return model, accuracy

def main():
    print("=" * 60)
    print("MLflow 자동 추적 데모")
    print("=" * 60)
    
    # MLflow 자동 로깅 활성화 - 이것만 추가!
    mlflow.sklearn.autolog()
    
    with mlflow.start_run(run_name="auto_tracking_demo"):
        model, accuracy = clean_train_model()
    
    print("\n🎉 완료!")
    print("MLflow UI에서 자동으로 추적된 내용을 확인하세요:")
    print("- 모델 파라미터 (자동)")
    print("- 성능 지표 (자동)")
    print("- 모델 파일 (자동)")
    print("- 피처 중요도 (자동)")

if __name__ == "__main__":
    main()
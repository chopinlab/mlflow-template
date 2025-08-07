#!/usr/bin/env python3
"""
MLflow만 사용한 간단한 테스트
"""
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def test_mlflow():
    print("🧪 MLflow 연결 테스트 시작")
    
    # MLflow 설정
    mlflow.set_tracking_uri("http://localhost:8080")
    
    try:
        # 실험 설정
        mlflow.set_experiment("mlflow_connection_test")
        print("✅ MLflow 서버 연결 성공")
        
        with mlflow.start_run(run_name="connection_test"):
            print("✅ MLflow 실행 시작 성공")
            
            # 간단한 데이터와 모델
            X, y = make_classification(n_samples=50, n_features=4, n_classes=2, random_state=42)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            
            model = RandomForestClassifier(n_estimators=5, random_state=42)
            model.fit(X_train, y_train)
            
            y_pred = model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            
            # MLflow에 기록
            mlflow.log_param("n_estimators", 5)
            mlflow.log_metric("accuracy", accuracy)
            
            print(f"✅ 모델 훈련 및 기록 완료 - 정확도: {accuracy:.4f}")
            print("📊 MLflow UI에서 확인: http://localhost:8080")
            
        return True
        
    except Exception as e:
        print(f"❌ MLflow 연결 실패: {e}")
        print("💡 Docker 컨테이너가 실행 중인지 확인하세요: docker-compose ps")
        return False

if __name__ == "__main__":
    success = test_mlflow()
    if success:
        print("🎉 MLflow 테스트 성공!")
    else:
        print("😞 MLflow 테스트 실패!")
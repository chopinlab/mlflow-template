#!/usr/bin/env python3
"""
Prefect 서버와 연결된 테스트
"""
import mlflow
import mlflow.sklearn
from prefect import flow, task
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import os

# Prefect 서버 설정 (Docker 컨테이너의 Prefect 서버 사용)
os.environ["PREFECT_API_URL"] = "http://localhost:4200/api"

# MLflow 설정
mlflow.set_tracking_uri("http://localhost:8080")

@task(name="Prefect 서버 연결 테스트")
def prefect_server_test():
    """Prefect 서버 연결 테스트 태스크"""
    print("🔗 Prefect 서버와 연결된 태스크 실행 중...")
    
    # MLflow 실험 설정
    mlflow.set_experiment("prefect_server_test")
    
    with mlflow.start_run(run_name="prefect_server_run"):
        # 간단한 데이터와 모델
        X, y = make_classification(n_samples=100, n_features=4, n_classes=2, random_state=42)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        model = RandomForestClassifier(n_estimators=10, random_state=42)
        model.fit(X_train, y_train)
        
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        # MLflow에 기록
        mlflow.log_param("n_estimators", 10)
        mlflow.log_param("test_type", "prefect_server_connected")
        mlflow.log_metric("accuracy", accuracy)
        
        print(f"✅ 모델 훈련 완료 - 정확도: {accuracy:.4f}")
        return accuracy

@flow(name="Prefect 서버 연결 플로우", log_prints=True)
def prefect_server_flow():
    """Prefect 서버에 등록될 플로우"""
    print("🚀 Prefect 서버와 연결된 플로우 시작")
    print(f"🔗 Prefect API URL: {os.environ.get('PREFECT_API_URL')}")
    
    accuracy = prefect_server_test()
    
    print(f"✅ 플로우 완료! 정확도: {accuracy:.4f}")
    print("📊 Prefect UI에서 확인: http://localhost:4200")
    print("📊 MLflow UI에서 확인: http://localhost:8080")
    
    return {
        "status": "success",
        "accuracy": accuracy,
        "message": "Prefect 서버와 성공적으로 연결됨!"
    }

if __name__ == "__main__":
    print("=" * 60)
    print("Prefect 서버 연결 테스트")
    print("=" * 60)
    print(f"Prefect API URL: {os.environ.get('PREFECT_API_URL')}")
    
    try:
        result = prefect_server_flow()
        print("=" * 60)
        print(f"최종 결과: {result}")
        print("=" * 60)
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        print("💡 Docker 컨테이너가 실행 중인지 확인하세요!")
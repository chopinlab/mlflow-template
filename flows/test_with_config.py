#!/usr/bin/env python3
"""
설정된 Prefect 서버로 플로우 실행
"""
import mlflow
import mlflow.sklearn
from prefect import flow, task
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# MLflow 설정 (localhost로 변경)
mlflow.set_tracking_uri("http://localhost:8080")

@task(name="설정된 서버 테스트")
def configured_test():
    """설정된 Prefect 서버에서 실행되는 태스크"""
    print("🎯 설정된 Prefect 서버에서 실행 중...")
    
    # MLflow 실험 설정
    mlflow.set_experiment("configured_server_test")
    
    with mlflow.start_run(run_name="configured_run"):
        # 데이터 생성 및 모델 훈련
        X, y = make_classification(n_samples=200, n_features=10, n_informative=5, n_classes=3, random_state=42)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        
        model = RandomForestClassifier(n_estimators=20, max_depth=5, random_state=42)
        model.fit(X_train, y_train)
        
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        # MLflow에 기록
        mlflow.log_param("n_estimators", 20)
        mlflow.log_param("max_depth", 5)
        mlflow.log_param("n_classes", 3)
        mlflow.log_param("server_type", "configured_docker")
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("train_samples", len(X_train))
        mlflow.log_metric("test_samples", len(X_test))
        
        print(f"✅ 모델 훈련 완료 - 정확도: {accuracy:.4f}")
        return {
            "accuracy": accuracy,
            "run_id": mlflow.active_run().info.run_id
        }

@flow(name="설정된 서버 플로우", log_prints=True)
def configured_server_flow():
    """설정된 Prefect 서버에서 실행될 플로우"""
    print("🚀 설정된 Prefect 서버 플로우 시작")
    print("📡 이 실행은 Prefect UI (http://localhost:4200)에서 확인할 수 있습니다!")
    
    result = configured_test()
    
    print(f"✅ 플로우 완료!")
    print(f"📊 정확도: {result['accuracy']:.4f}")
    print(f"🔗 MLflow Run ID: {result['run_id']}")
    print("📊 Prefect UI: http://localhost:4200")
    print("📊 MLflow UI: http://localhost:8080")
    
    return result

if __name__ == "__main__":
    print("=" * 60)
    print("설정된 Prefect 서버로 플로우 실행")
    print("=" * 60)
    
    try:
        result = configured_server_flow()
        print("=" * 60)
        print(f"🎉 성공! 결과: {result}")
        print("이제 Prefect UI에서 실행 내역을 확인할 수 있습니다!")
        print("=" * 60)
    except Exception as e:
        print(f"❌ 오류: {e}")
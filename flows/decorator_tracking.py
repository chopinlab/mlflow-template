#!/usr/bin/env python3
"""
데코레이터 방식 - 함수에 @track 만 붙이면 자동 추적
"""
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from functools import wraps

# MLflow 설정
mlflow.set_tracking_uri("http://localhost:8080")

def track_ml_experiment(experiment_name="auto_experiment"):
    """
    데코레이터: 함수에 붙이면 자동으로 MLflow 추적
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            mlflow.set_experiment(experiment_name)
            mlflow.sklearn.autolog()
            
            with mlflow.start_run(run_name=func.__name__):
                result = func(*args, **kwargs)
                print(f"✅ {func.__name__} 실행 완료 - 자동 추적됨!")
                return result
        return wrapper
    return decorator

# 사용법: @track_ml_experiment만 붙이면 끝!
@track_ml_experiment(experiment_name="decorator_demo")
def train_livestock_classifier():
    """
    축산업 분류 모델 훈련 - 깔끔한 코드!
    """
    print("🐄 축산업 분류 모델 훈련 중...")
    
    # 축산업 데이터 시뮬레이션
    X, y = make_classification(
        n_samples=1000, 
        n_features=15, 
        n_informative=10,
        n_classes=3,  # A, B, C 등급
        random_state=42
    )
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )
    
    # 모델 훈련 (추적 코드 없음!)
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=12,
        min_samples_split=5,
        random_state=42
    )
    
    model.fit(X_train, y_train)
    
    # 평가
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"📊 등급 분류 정확도: {accuracy:.4f}")
    
    return {
        "model": model,
        "accuracy": accuracy,
        "train_samples": len(X_train),
        "test_samples": len(X_test)
    }

@track_ml_experiment(experiment_name="weight_estimation")
def train_weight_estimator():
    """
    체중 추정 모델 - 또 다른 예시
    """
    print("⚖️ 체중 추정 모델 훈련 중...")
    
    # 회귀 문제로 시뮬레이션
    from sklearn.datasets import make_regression
    
    X, y = make_regression(
        n_samples=800,
        n_features=8,
        noise=0.1,
        random_state=42
    )
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )
    
    # 회귀 모델
    from sklearn.ensemble import RandomForestRegressor
    model = RandomForestRegressor(n_estimators=80, random_state=42)
    model.fit(X_train, y_train)
    
    # 평가
    from sklearn.metrics import mean_squared_error, r2_score
    y_pred = model.predict(X_test)
    
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"📊 R² Score: {r2:.4f}")
    print(f"📊 MSE: {mse:.4f}")
    
    return {
        "model": model,
        "r2_score": r2,
        "mse": mse
    }

def main():
    print("=" * 60)
    print("데코레이터 방식 MLflow 추적")
    print("=" * 60)
    
    # 1. 분류 모델 훈련
    print("\n1️⃣ 등급 분류 모델")
    result1 = train_livestock_classifier()
    
    # 2. 회귀 모델 훈련  
    print("\n2️⃣ 체중 추정 모델")
    result2 = train_weight_estimator()
    
    print("\n🎉 모든 실험 완료!")
    print("📊 MLflow UI에서 두 실험 모두 확인 가능: http://localhost:8080")
    
    return {
        "classification": result1,
        "regression": result2
    }

if __name__ == "__main__":
    results = main()
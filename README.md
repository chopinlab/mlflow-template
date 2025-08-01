# MLflow 모델 학습 템플릿

MLflow를 활용한 머신러닝 모델 학습 및 실험 추적 템플릿입니다. UV 패키지 관리자를 사용하여 빠르고 안정적인 개발 환경을 제공합니다.

## 🚀 주요 기능

- **MLflow 실험 추적**: 자동화된 파라미터, 메트릭, 아티팩트 로깅
- **완전한 ML 파이프라인**: 데이터 생성부터 모델 평가까지
- **UV 패키지 관리**: 빠르고 안정적인 의존성 관리
- **시각화**: Feature importance 차트 자동 생성
- **모델 레지스트리**: 학습된 모델 자동 등록

## 📋 요구사항

- Python 3.8 이상
- UV 패키지 관리자

## ⚡ 빠른 시작

### 1. UV 설치
```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Homebrew (macOS)
brew install uv
```

### 2. 프로젝트 설정
```bash
# 저장소 클론
git clone <repository-url>
cd mlflow-template

# 의존성 설치
uv sync
```

### 3. 모델 학습 실행
```bash
# 방법 1: 스크립트 사용 (권장)
./run.sh

# 방법 2: 직접 실행
uv run python train.py

# 방법 3: 특정 Python 버전 사용
uv run --python 3.13 python train.py
```

### 4. MLflow UI 실행
```bash
uv run mlflow ui
```
브라우저에서 http://localhost:5000 접속하여 실험 결과를 확인하세요.

## 📊 프로젝트 구조

```
mlflow-template/
├── train.py              # 메인 학습 스크립트
├── run.sh                # 실행 스크립트
├── pyproject.toml        # 프로젝트 설정 및 의존성
├── CLAUDE.md             # Claude Code 가이드
├── docs/
│   └── uv-usage.md       # UV 사용법 상세 가이드
├── mlruns/               # MLflow 실험 데이터 (자동 생성)
└── feature_importance.png # Feature importance 차트 (자동 생성)
```

## 🔧 아키텍처

### 데이터 파이프라인
- **데이터 생성**: `create_sample_data()` - 1000개 샘플, 20개 피처의 분류 데이터셋
- **전처리**: StandardScaler를 사용한 피처 정규화
- **분할**: 80:20 train/test 분할

### 모델링
- **알고리즘**: RandomForestClassifier
- **하이퍼파라미터**: n_estimators, max_depth, min_samples_split
- **평가 지표**: accuracy, precision, recall, f1_score

### MLflow 통합
- **실험 이름**: "ml_experiment"
- **로깅 항목**:
  - 파라미터: 모델 하이퍼파라미터, 데이터셋 크기
  - 메트릭: 성능 지표들
  - 아티팩트: feature importance 시각화
  - 모델: 학습된 모델과 전처리기

## 🎯 사용 예시

### 하이퍼파라미터 튜닝
```python
# train.py에서 파라미터 수정
rf = RandomForestClassifier(
    n_estimators=200,      # 기본값: 100
    max_depth=15,          # 기본값: 10
    min_samples_split=5,   # 기본값: 2
    random_state=42
)
```

### 다른 데이터셋 사용
```python
# create_sample_data() 함수 수정
def create_sample_data():
    X, y = make_classification(
        n_samples=2000,        # 샘플 수 증가
        n_features=30,         # 피처 수 증가
        n_informative=25,      # 유용한 피처 수
        n_redundant=5,         # 중복 피처 수
        random_state=42
    )
    return X, y
```

### 추가 메트릭 로깅
```python
from sklearn.metrics import roc_auc_score

# 모델 평가 후 추가
auc_score = roc_auc_score(y_test, model.predict_proba(X_test_scaled)[:, 1])
mlflow.log_metric("auc", auc_score)
```

## 📈 실험 결과 분석

MLflow UI에서 다음 정보를 확인할 수 있습니다:

1. **실험 비교**: 여러 실행 간 성능 비교
2. **파라미터 영향**: 하이퍼파라미터 변화에 따른 성능 변화
3. **모델 아티팩트**: Feature importance 차트, 모델 파일
4. **메트릭 히스토리**: 시간에 따른 성능 변화 추이

## 🛠️ 개발 가이드

### 새로운 모델 추가
1. `train_model()` 함수에서 모델 변경
2. 해당 모델에 맞는 하이퍼파라미터 설정
3. 필요시 전처리 파이프라인 수정

### 새로운 메트릭 추가
1. sklearn.metrics에서 필요한 메트릭 import
2. 모델 평가 섹션에서 계산
3. `mlflow.log_metric()`으로 로깅

### 커스텀 시각화 추가
1. matplotlib/seaborn으로 차트 생성
2. 파일로 저장
3. `mlflow.log_artifact()`로 업로드

## 🔍 문제 해결

### 의존성 문제
```bash
# 캐시 정리 후 재설치
uv cache clean
uv sync --reinstall
```

### MLflow UI 접속 불가
```bash
# 포트 확인
lsof -i :5000

# 다른 포트 사용
uv run mlflow ui --port 5001
```

### Python 버전 문제
```bash
# 사용 가능한 버전 확인
uv python list

# 특정 버전 설치
uv python install 3.13
```

## 📚 참고 자료

- [MLflow 공식 문서](https://mlflow.org/docs/latest/index.html)
- [UV 사용법 가이드](docs/uv-usage.md)
- [scikit-learn 문서](https://scikit-learn.org/stable/)
- [Python 3.13 Free-threading](https://docs.python.org/3.13/whatsnew/3.13.html#free-threaded-cpython)

## 📄 라이선스

MIT License

## 🤝 기여하기

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: 새로운 기능 추가'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
# UV 패키지 매니저 사용법

이 프로젝트는 UV를 사용하여 Python 패키지를 관리합니다. UV는 pip와 virtualenv를 대체하는 빠르고 안정적인 패키지 관리 도구입니다.

## UV 설치

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Homebrew (macOS)
brew install uv

# pipx
pipx install uv
```

## 기본 사용법

### 프로젝트 초기화
```bash
# 새 프로젝트 생성
uv init my-project
cd my-project

# 기존 프로젝트에 uv 설정 추가
uv init
```

### 가상환경 관리
```bash
# 가상환경 생성 및 패키지 설치
uv sync

# 특정 Python 버전으로 가상환경 생성
uv sync --python 3.11

# 가상환경 활성화 없이 명령 실행
uv run python script.py
uv run pytest
```

### 패키지 관리
```bash
# 패키지 추가
uv add mlflow
uv add scikit-learn

# 개발 의존성 추가
uv add --dev pytest black

# 패키지 제거
uv remove package-name

# 패키지 업그레이드
uv sync --upgrade
```

### 실행 명령어
```bash
# Python 스크립트 실행
uv run python train.py

# 모듈 실행
uv run -m mlflow ui

# Jupyter 실행
uv run jupyter lab
```

## 이 프로젝트에서의 UV 사용

### 1. 초기 설정
```bash
# 의존성 설치
uv sync
```

### 2. 모델 학습 실행
```bash
# 방법 1: 스크립트 사용
./run.sh

# 방법 2: 직접 실행
uv run python train.py
```

### 3. MLflow UI 실행
```bash
uv run mlflow ui
```

### 4. Jupyter 노트북 사용
```bash
uv run jupyter lab
```

## UV vs PIP 비교

| 기능 | UV | PIP |
|------|----|----|
| 속도 | 매우 빠름 (Rust 기반) | 보통 |
| 가상환경 관리 | 내장 | 별도 도구 필요 |
| Lock 파일 | uv.lock 자동 생성 | requirements.txt 수동 관리 |
| Python 버전 관리 | 내장 | pyenv 등 필요 |
| 설정 파일 | pyproject.toml | requirements.txt |

## 자주 사용하는 명령어

```bash
# 현재 환경 정보 확인
uv info

# 설치된 패키지 목록
uv list

# 패키지 트리 구조 보기
uv tree

# 캐시 정리
uv cache clean

# 환경 변수와 함께 실행
uv run --env-file .env python train.py
```

## 문제 해결

### 패키지 설치 오류
```bash
# 캐시 삭제 후 재설치
uv cache clean
uv sync --reinstall
```

### Python 버전 문제
```bash
# 사용 가능한 Python 버전 확인
uv python list

# 특정 버전 설치
uv python install 3.11
```

### 권한 문제
```bash
# 사용자 권한으로 설치
uv sync --user
```

## Python 버전 관리

UV는 Python 버전 관리도 지원합니다. pyenv 없이도 다양한 Python 버전을 쉽게 설치하고 관리할 수 있습니다.

### Python 버전 확인
```bash
# 현재 사용 중인 Python 버전
python3 --version
uv run --no-project python --version

# 설치된 모든 Python 버전 확인
uv python list --only-installed

# 사용 가능한 모든 Python 버전 확인
uv python list
```

### Python 설치 및 관리
```bash
# 특정 버전 설치
uv python install 3.13
uv python install 3.12
uv python install 3.11

# Python 3.13 Free-threaded (NoGIL) 설치
uv python install 3.13.5+freethreaded

# 최신 버전 설치
uv python install 3.13
```

### 프로젝트별 Python 버전 지정
```bash
# 프로젝트에 Python 버전 고정
uv python pin 3.13

# 특정 버전으로 가상환경 생성
uv sync --python 3.13

# 특정 버전으로 명령 실행
uv run --python 3.13 python script.py
uv run --python 3.12 python script.py
```

### .python-version 파일
```bash
# 프로젝트 루트에 .python-version 파일 생성
echo "3.13" > .python-version

# UV가 자동으로 해당 버전 사용
uv sync
```

### Python 버전별 특징 비교

| 버전 | 주요 특징 | 사용 권장 |
|------|-----------|-----------|
| 3.13 | NoGIL 지원, JIT 컴파일러 | 최신 기능 실험 |
| 3.12 | 성능 향상, f-string 개선 | 일반적 사용 |
| 3.11 | 큰 성능 향상 (10-60%) | 안정성 중시 |
| 3.10 | Pattern matching | 레거시 호환 |

### Free-threaded Python (NoGIL) 사용법
```bash
# Free-threaded 버전 설치
uv python install 3.13.5+freethreaded

# Free-threaded로 실행
uv run --python 3.13.5+freethreaded python script.py

# GIL 상태 확인
uv run --python 3.13.5+freethreaded --no-project python -c "
import sys
print(f'Free-threading: {hasattr(sys.flags, \"gil\")}')
if hasattr(sys.flags, 'gil'):
    print(f'GIL disabled: {sys.flags.gil == 0}')
"
```

### 팀 개발에서의 Python 버전 관리
```bash
# 팀 전체가 동일한 버전 사용
uv python pin 3.13

# .python-version 파일을 git에 커밋
git add .python-version
git commit -m "fix: Python 버전 3.13으로 고정"

# 팀원들이 프로젝트 클론 후
uv sync  # 자동으로 지정된 Python 버전 사용
```

### 버전 호환성 주의사항
```bash
# Free-threaded 버전은 실험적 기능
# 일부 패키지가 호환되지 않을 수 있음
# 프로덕션에서는 일반 버전 사용 권장

# 호환성 문제 발생 시
uv python pin 3.13  # 일반 버전으로 변경
uv sync --reinstall
```

## 추가 리소스

- [UV 공식 문서](https://docs.astral.sh/uv/)
- [UV GitHub 저장소](https://github.com/astral-sh/uv)
- [Migration Guide](https://docs.astral.sh/uv/guides/migrate-from-pip/)
- [Python 3.13 Free-threading 가이드](https://docs.python.org/3.13/whatsnew/3.13.html#free-threaded-cpython)
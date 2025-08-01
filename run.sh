#!/bin/bash

# MLflow 모델 학습 템플릿 실행 스크립트

echo "MLflow 모델 학습 템플릿 실행 중..."

# 의존성 설치 (필요한 경우)
echo "1. 의존성 설치 중..."
pip install -r requirements.txt

# 모델 학습 실행
echo "2. 모델 학습 시작..."
python train.py

echo "3. 학습 완료!"
echo ""
echo "MLflow UI를 실행하려면 다음 명령어를 실행하세요:"
echo "mlflow ui"
echo ""
echo "브라우저에서 http://localhost:5000 접속하여 실험 결과를 확인하세요."
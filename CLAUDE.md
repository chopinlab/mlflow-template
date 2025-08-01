# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an MLflow-based machine learning template for rapid model training and experiment tracking. The project demonstrates a complete ML pipeline with synthetic data generation, model training, evaluation, and experiment tracking using MLflow.

## Architecture

- **train.py**: Main training script containing the complete ML pipeline
  - `create_sample_data()`: Generates synthetic classification dataset (1000 samples, 20 features)
  - `train_model()`: Handles data preprocessing, model training, evaluation, and MLflow logging
  - `main()`: Orchestrates the entire pipeline
- **MLflow Integration**: Automatic experiment tracking, parameter/metric logging, model registration, and artifact storage
- **Model**: RandomForestClassifier with configurable hyperparameters
- **Preprocessing**: StandardScaler for feature normalization

## Common Commands

### Setup and Installation
```bash
pip install -r requirements.txt
```

### Run Training
```bash
# Method 1: Using the run script
./run.sh

# Method 2: Direct execution
python train.py
```

### MLflow UI
```bash
mlflow ui
# Access at http://localhost:5000
```

## MLflow Experiment Structure

- **Default Experiment**: "ml_experiment"
- **Logged Parameters**: n_estimators, max_depth, min_samples_split, train/test sample counts
- **Logged Metrics**: accuracy, precision, recall, f1_score
- **Artifacts**: feature_importance.png visualization
- **Models**: RandomForestClassifier and StandardScaler saved to model registry

## Key Files Generated During Training

- `mlruns/`: MLflow experiment tracking data
- `feature_importance.png`: Feature importance visualization (logged as artifact)

## Modifying the Template

- To change the model: Modify the RandomForestClassifier initialization in `train_model()`
- To adjust data: Modify parameters in `create_sample_data()` 
- To add metrics: Add new metric calculations and `mlflow.log_metric()` calls
- To change experiment name: Pass different `experiment_name` to `train_model()`



## Git Commit Guidelines
- When creating commits, remove any Anthropic/Claude attribution footers or co-author information
- Keep commit messages clean and focused on the actual changes
- Use conventional commit format with Korean descriptions: "feat: 새로운 기능 추가", "fix: 버그 수정", "docs: 문서 업데이트" etc.
- Follow conventional commit format (feat:, fix:, docs:) with Korean commit messages for better team communication
- Reference the updated README.md for project-specific guidelines and setup instructions
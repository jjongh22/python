from sklearn.datasets import fetch_openml
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

# OpenML에서 Yeast 데이터셋 로드
yeast = fetch_openml('yeast', version=4, as_frame=True)  # 데이터를 DataFrame 형태로 로드
X = yeast['data']  # 특성 데이터
y = yeast['target']  # 타겟 데이터

# 데이터 크기 확인
print(f"Data shape: {X.shape}, Target shape: {y.shape}")  # (2417, 103), (2417, 14)

# 타겟 데이터를 numpy 배열로 변환 (다중 클래스 멀티아웃풋 처리)
y = np.array(y)

# 학습 데이터와 테스트 데이터로 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 랜덤 포레스트 모델 생성 (불균형 데이터 처리를 위해 class_weight='balanced' 사용)
rf_model = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)

# 각 클래스에 대해 개별적으로 모델을 학습하고 평가
n_classes = y.shape[1]  # 타겟 출력 클래스 수
for i in range(n_classes):
    print(f"\nTraining for output class {i + 1}/{n_classes}...")
    
    # 각 클래스에 대해 모델 학습
    rf_model.fit(X_train, y_train[:, i])  # 해당 클래스에 대해 학습
    y_pred = rf_model.predict(X_test)    # 해당 클래스에 대해 예측
    
    # 정확도 및 분류 리포트 출력
    accuracy = accuracy_score(y_test[:, i], y_pred)  # 정확도 계산
    print(f"Accuracy for class {i + 1}: {accuracy:.4f}")
    
    # 분류 리포트 출력 (zero_division=0 추가)
    print(f"Classification Report for class {i + 1}:\n{classification_report(y_test[:, i], y_pred, zero_division=0)}")

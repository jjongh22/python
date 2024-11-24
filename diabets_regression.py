import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.linear_model import Lars
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# 데이터 로드
diabetes = load_diabetes()  # 당뇨병 데이터셋 로드
X, y = diabetes.data, diabetes.target  # 입력 변수 X와 타겟 변수 y 분리

# 학습 데이터와 테스트 데이터로 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# 데이터를 학습용(80%)과 테스트용(20%)으로 나눔
# random_state는 결과 재현성을 위해 설정

# LARS 회귀 모델 생성 및 학습
lars_model = Lars(n_nonzero_coefs=10)  # 최대 10개의 변수만 선택하도록 설정
lars_model.fit(X_train, y_train)  # 학습 데이터를 사용해 모델 학습

# 예측
y_pred = lars_model.predict(X_test)  # 테스트 데이터에 대한 예측값 계산

# 평가
mse = mean_squared_error(y_test, y_pred)  # 평균 제곱 오차 계산
r2 = r2_score(y_test, y_pred)  # 결정 계수(R^2) 계산

# 결과 출력
print("Mean Squared Error (MSE):", mse)  # MSE 출력
print("R-squared (R2):", r2)  # R2 출력
print("Selected features:", lars_model.active_)  # LARS가 선택한 피처의 인덱스 출력

# 실제 값과 예측 값 시각화
plt.scatter(y_test, y_pred, alpha=0.7, color="blue")  # 실제 값과 예측 값 산점도
plt.plot([0, 330], [0, 330], '--r', linewidth=2)  # 이상적인 예측선(기울기 1) 표시
plt.xlabel("Actual")  # x축 레이블 설정
plt.ylabel("Predicted")  # y축 레이블 설정
plt.title("LARS Regression")  # 그래프 제목 설정
plt.grid()  # 격자 추가
plt.show()  # 그래프 출력

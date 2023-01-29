# 문제1 : 머신러닝을 사용해서 300명이 방문했을 때 판매량을 예측해보세요

# 머신러닝 라이브러리
import sklearn

#그래프 라이브러리
import matplotlib.pyplot as plt

# 수학/과학 계산 라이브러리
import  numpy as np

# 다차원 데이터 모듈
import pandas as pd
from sklearn.linear_model import LinearRegression           # 1차원 머신러닝

원본데이터 = pd.read_csv('kyobo.csv', encoding='cp949')
print(원본데이터.head(5))

x = 원본데이터.iloc[:,:-1].values            
y = 원본데이터.iloc[:,-1].values

선형기계학습 = LinearRegression()
선형기계학습.fit(x, y)

a = int(input('방문자수를 입력해주세요:')) 
y_pred = 선형기계학습.predict(x)
result = 선형기계학습.predict([[a]])

print('예측한 y값:\n',y_pred)
print('AI예측값:',선형기계학습.predict([[a]]),'건')
print('AI예측값:',round(result[0]),'건')                # 소수점 반올림 적용

plt.scatter(x, y, color='green')            
plt.plot(x, y_pred, color='red')            
plt.title('kyobo')        
plt.xlabel('number of visitors')                         
plt.ylabel('sales rate')                  
plt.show()


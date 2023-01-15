import matplotlib.pyplot as plt        # 파이썬에서 제공해주는 기능 그래프를 그려주는 라이브러리(부속품)


# 문제 : 80점 이상인 사람의 수

시험점수 = [71, 81, 77, 81, 99, 23, 55, 100, 0]

_80점이상 = []

# 1. 시험점수 중 80점 이상만 _80점이상 리스트로 옮기고
# 2. 80점이상의 길이(갯수) 구한다.


for i in 시험점수:
    if i >= 80:
        _80점이상.append(i)

print(_80점이상)
print(len(_80점이상),'명')


# 데이터 시각화 - 참고하기
plt.title('test')               # 제목
plt.xlabel('score')             # x축
plt.ylabel('person')            # y축
plt.hist(시험점수)               # 막대그래프                     
plt.show()                      # 그래프를 띄워준다.



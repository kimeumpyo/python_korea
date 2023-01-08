# 연산자 (숫자)
a = 10
b = 3


a + b           # 덧셈 13
a - b           # 뺼셈 7
a * b           # 곱셈 30
a / b           # 나눗셈 3.3
a % b           # 나머지구하기 1
a ** b          # a의 b제곱  8

a = b           # b값을 a공간에 대입
a == b          # 같다 (수학의 = )
a != b          # 다르다
a > b           # a 가 크다
a < b           # a 가 작다
a >= b          # a 가 b보다 크거나 같다
a <= b          # a 가 b보다 작거나 같다

# 대입연사자 주의할 점 =
a = a           # 왼쪽은 공간의 개녕으로 a, 오른쪽은 a 안에 들어있는 값

a += b          # a = a + b
a -= b          # a = a - b
a *= b          # a = a * b
a /= b          # a = a / b

(a + b) * a     # 우선순위

# 비교연산자 ==, >=, > ture 또는 False 로 알려준다.
a = 10
b = 3
print(a != b)   # 10은 3과 다르다. 
print(a == b)   #  False (거짓)
print(a > b)    # 10 > 3 --> Ture(참)

# 관계연산자 and, or, not

a > 5 and a < 15         # a 는 5보다 크고 15보다 작다

print(a > 5 and a < 15)  # True

a < 0 or a > 5           # a는 0보다 작거나 5보다 크다
print(a < 0 or a > 5)    # True

# and : 둘다 맞아야만 맞고 나머지는 다 틀림
# or : 둘 중 하나만 맞아도 맞음

print(a < 0 and a > 5)   # a는 0보다 작지않아서  False
print(a < 0 or a > 100)  # 둘다 틀려서 Flase
print(not b==3)          # False는 True로, True는 False로 


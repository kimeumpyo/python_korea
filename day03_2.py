# 반복문 (while, for)

# for를 사용해서 hello 3번하기
# for 임시변수 in range(3):
#     print('hello')

# # 임시변수 :  while에서 i를 값으로 사용 ==> 임시변수
i = 0
while i < 3:
    print(i,'번째 Hello')
    i += 1

for j in range(3):
    print(j, '번째 Hello')

# i = 1
for i in range(1, 4):           # 1 ~ 3 Hello
    print(i, '번째 Hello')

range(3) == range(0, 3)       # 0 ~ 2

# 1월
# 2월
# 3월
# 4월
# 5월
# ~~~~
# 12월

for i in range(1, 13):
    print(i,'월')

# for i in range(7, 101, 7):
#     print(i)

# for j in range(0, 11, 2):
#     print(j)


# 문제1
'''
5
4
3
2
1
'''
for i in range(5, 0, -1):
    print(i)

# 다른방법1
num = 5
for i in range(5):
    print(num)
    num -= 1

# 다른방법2
for i in reversed(range(1, 6)):
    print(i)

# 문제2

'''
양의 정수 1개를 입력받아서
1 부터 입력한 숫자까지 합계를 알려주는 프로그램

ex) 10 
1 ~ 10을 모두 더해서 55
ex) 9
1 ~ 9를 모두 더해서 45

'''
count = int(input('양의 정수를 입력하세요:'))
sum = 0   

for i in range(1, count+1):
    sum += i
print (sum)

# 문제3

num1 = 1
num2 = 2
backup = 0
backup = num1
num1 = num2
num2 = backup
print(num1, num2)
    
    

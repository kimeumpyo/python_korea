# 1
# 횟수를 입력받아서 그 수만큼 Hello 출력하는 프로그램
# 5 를 입력하면
# 1번째 Hello
# 2번째 Hello
# 3번째 Hello
# 4번째 Hello
# 5번째 Hello

# i = 1
# a = int(input('몇번까지 반복할지 입력해주세요:'))
# while i <= a:
#     print(i,'번쨰 Hello')
#     i += 1
# print('=======')


# 2
# 1~100 사이에서 7의 배수만 출력하는 프로그램 (while안에서 if를 사용)

# a = int(input('숫자를 지정해주세요:'))
# b = int(input('몇배수의 숫자를 출력할지 적어주세요:'))
# i = b 
# while i <= a :
#     if i % b == 0 :
#         print(i,'번쨰 Hello')
#     i += 1          
# print('=======')

# 3
# 커피 1잔에 300원, 금액을 입력하여 총 몇잔의 커피와 잔돈이 얼마가 남는지 출력
# ==실행 예==
# 금액은 얼마인가요>> 1400원
# 커피 1잔, 잔돈 1100원
# 커피 2잔, 잔돈 800원
# 커피 3잔, 잔돈 500원
# 커피 4잔, 잔돈 200원

m = int(input('지불한 금액을 적어주세요:'))
cf = int(input('커피값을 입력해주세요:'))
i = 1

while i * cf < m : 
    e = m - (i * cf)
    print('커피',i,'잔, 잔돈',e,'원')
    i += 1     
print ('=================')





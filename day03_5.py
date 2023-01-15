# 문자열 = 'hello world, my name is python'
# 정수 = 314
# 실수 = 3.14

# for i in  문자열:
#     print(i, end=' ')

# print()

# i = 0
# while i < len(문자열):
#     print(문자열[i], end=' ')
#     i += 1

# # str, int, float, list, tuple, dict, set
# # 리스트
# # 지하철 3칸, [10, 15, 12]
# subway1 = 10
# subway1 = 10
# subway1 = 10
# print()
# 리스트 = [10, 15, 12, 11, 22, 33, 44, 55, 66]
# for i in  리스트:
#     print(i, '명')


# 문제1 : 문자열에서 알파벳 o 의 갯수를 알려주세요           

문자열 = 'hello world, my name is python'             #print(문자열.count('o'),'개')

o_count = 0
for i in 문자열:
    if i == 'o':
        o_count += 1
print(o_count)        

# 문제2 : 1월 ~ 12월을 출력하되 입력받은 월은 skip

a = int(input('시작월을 입력해주세요>>'))
b = int(input('종료될월을 입력해주세요>> '))
skip_month = int(input('몇 월을 스킵할까요?>>'))
for i in range(a, b+1):
    if i == skip_month:
        continue
    print(i,'월')
   
# 문제3 : 1월 ~ 12월을 출력하되 입력받은 월로부터는 출력안함

break_month = int(input('몇 월까지 스킵할까요?>>'))
for i in range(1, 13):
    if i == break_month:
        break
    print(i,'월')


# 문제4 : 구구단을 만들어주세요
for i in range(2,10):
    for j in range(1,10):
        print(i, "x", j, "=", i*j, end= '\t')
    print()                                            # 줄바꿈 
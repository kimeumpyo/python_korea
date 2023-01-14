# 문자열 = 'hello world, my name is python'
# 정수 = 314
# 실수 = 3.14

# for i in  문자열:
    # print(i, end=' ')

# print()

# i = 0
# while i < len(문자열):
#     print(문자열[i], end=' ')
#     i += 1

# str, int, float, list, tuple, dict, set
# 리스트
# 지하철 3칸, [10, 15, 12]
# subway1 = 10
# subway2 = 15
# subway3 = 12
# print()
# 리스트 = [10, 15, 12, 11, 22, 33, 44, 55, 66]
# for i in  리스트:
#     print(i, '명')


# 문제1 : 문자열에서 알파벳 o 의 갯수를 알려주세요           

# 문자열 = 'hello world, my name is python'

# print(문자열.count('o'),'개')

#=========================

# 문자열 = 'hello world, my name is python'
# a = {}
# for i in  문자열:
#     if i in a:
#         a [i] += 1
#     else :
#         a [i] = 1
# print(a)        

#=========================

문자열 = 'hello world, my name is python'

for i in 문자열:
    if i == 'o':
        a = print(i, end=',')
        list = [a]
        print(len(list))

# for i in 문자열:
#     if i == 'o':
#         a = print(i, end=',')
#         list = [a]
#         print(len(list))

        
          
# ========================

# a = 0
# for i in 문자열:
#     if i == 'o':
#         print(i += 1)
      
#=========================

# for i in  문자열:
#     if i == o:
#         o = 1
#         print( i, end = '+',)



# 문제2 : 1월 ~ 12월을 출력하되 입력받은 월은 skip

# a = int(input('시작월을 입력해주세요>>'))
# b = int(input('종료될월을 입력해주세요>> '))
# for i in range(a, b+1):
#     print(i,'월')

# 문제3 : 1월 ~ 12월을 출력하되 입력받은 월로부터는 출력안함


# 문제4 : 구구단을 만들어주세요
# for i in range(2,10):
#     for j in range(1,10):
#         print(i, "x", j, "=", i*j)
#     print()
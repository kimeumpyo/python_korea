# 20세 이상은 성인
# 14세 이상은 청소년
# 14세 미만은 어린이


# 나이 = input('나이를 입력해주세요:')

# if int(나이) >= 20 :
#     print('성인 입니다')
# elif int(나이) >= 14 and int(나이) < 20:        #위에 있는if가 틀렸다는 가정하에실행
#     print('청소년 입니다.')
# else :
#     print('어린이 입니다.')

# 방법1
# 나이 = input('나이를 입력해주세요:')

# if int(나이) >= 23:
#     print('회사원 입니다')
# elif int(나이) >= 20 and int(나이) < 23:
#     print('대학생 입니다.')
# elif int(나이) >= 17 and int(나이) < 20:
#     print('고등학생 입니다.')
# elif int(나이) >= 14 and int(나이) < 17:
#     print('중학생 입니다.')
# elif int(나이) >= 8 and int(나이) < 14:
#     print('초등학생 입니다.')
# elif int(나이) >= 0 and int(나이) < 8:
#     print('유치원생 입니다.')


# 방법2
# 나이 = int(input('나이를 입력해주세요:'))

# if 나이 >= 23:
#     print('회사원 입니다')
# elif 나이 >= 20 and 나이 < 23:
#     print('대학생 입니다.')
# elif 나이 >= 17 and 나이 < 20:
#     print('고등학생 입니다.')
# elif 나이 >= 14 and 나이 < 17:
#     print('중학생 입니다.')
# elif 나이 >= 8 and 나이 < 14:
#     print('초등학생 입니다.')
# elif 나이 >= 0 and 나이 < 8:
#     print('유치원생 입니다.')

# 방법3
나이 = int(input('나이를 입력해주세요:'))# 정보를 받을때 int() 로 받아주면 문자가 아닌 숫자로 인식한다.

if 나이 >= 25:
    print('회사원 입니다')
elif 나이 >= 20: 
    print('대학생 입니다.')    # 위의 명령 조건이 걸러져있기 때문에 20~24살 범위가 실행이 가능하다.
elif 나이 >= 17: 
    print('고등학생 입니다.')
elif 나이 >= 14: 
    print('중학생 입니다.')
elif 나이 >= 8: 
    print('초등학생 입니다.')
elif 나이 >= 0:
    print('유치원생 입니다.')
else :
    print('?') 



     
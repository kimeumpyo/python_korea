# 조건문  if
# if 조건식:
# 조건식이 맞으면 실행할 문장

나이 = input('나이를 입력해주세요:')
if int(나이) >= 20:
    print('성인입니다.')
elif int(나이) < 20 and int(나이) > 13:
     print('미성년자 입니다.')
else:
    print('어린이 입니다.')

# if~elif~else
# if : 조건에 맞으면 실행
# elif : 위에 조건문이 틀리면 실행하는 조건문
# else : 조건문이 틀리면 문장 실행 

# 물온도 =
# 물온도가 100도 이상이면 '기체'
# 물 온도가 100도 미만이면 '액체'

물온도 = input('기체 온도는 몇도인가요?:')

if int(물온도) >= 100:                          # 100 이상
    print('기체')
elif int(물온도) <0:
    print('고체')
elif int(물온도) < 100 and int(물온도) >=0:
    print('액체')
else:
    print('나머지')



# if int(물온도) >= 100:
#     print('기체')
# if int(물온도) < 100 and int(물온도) >=0:       # 범위 0~99
#     print('액체')
# if int(물온도) <0:
#     prinf('고체')


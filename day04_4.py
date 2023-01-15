# 문자열을 저장하는 리스트
lst = []
num = 0


# 사용자에게 입력을 받아 리스트를 구성
# 1: 추가하기, 2: 수정하기, 3: 삭제하기, 4: 전체보기
while True:
    num = int(input('1:추가, 2:수정, 3:삭제, 4:조회:'))
    if num == 1:
        print(lst)
        (lst.append(input('추가할 값을 입력하세요:')))       
        print(lst)  
                    # 추가할 값을 추가
    elif num == 2:
        print(lst)
        try:
            a = (input('수정할 데이터를 입력해주세요:'))
            idx=lst.index(a)
            b = (input('수정할 데이터를 입력해주세요:'))
            lst[idx] = (b) 
            print(lst)
        except:
            print('오류가 발생했습니다.')
            
                        # 값을 수정 (수정하고자하는 값, 수정할 값)
    elif num == 3:
        print(lst)
        try:
            (lst.remove(input('삭제할 데이터를 입력해주세요:')))
            print(lst)
        except:
            print('오류가 발생했습니다.')
            
                    # 삭제할 값 입력
    elif num == 4:
        for i in lst:
            print(i)
                    # 전체조회
    elif num == 0:
        break           # 프로그램 종료
    else:
        print('없는 번호입니다.')



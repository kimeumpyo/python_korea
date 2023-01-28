# return : 함수의 결과를 활용할 수 있게 해준다
def 절댓값더하기(a,b):
    if a < 0:
        a *= -1
    if b < 0:
        b *= -1
    return a+b              # return 옆에 있는 값이 사용한 곳으로 전달 

결과1 = 절댓값더하기(3, 7)              # 10              
결과2 = 절댓값더하기(-4,결과1)              # 7
print(결과2)
print(절댓값더하기(-1,-1))

# 문제1

lst = [10,20,30,40,50]

def 총합(a_lst):
    return sum(a_lst)
    

sum = 총합(lst)
avg = int(sum/len(lst))

print('총합은',sum)
print('평균은',avg)

# 문제1

def 총합(a_lst):
    result = 0              # 함수 안에서 만든 변수는 함수가 끝나면 사라진다(지역변수)
    for i in lst:
        result += i
    return result
    
lst = [10,20,30,40,50]
sum = 총합(lst)
avg = int(sum/len(lst))

print('총합은',sum)
print('평균은',avg)

# 문제2 : 입력한 갯수만큼 *을 표시하는 함수

def star(num):
    result = ''
    for i in range(num):
        result += '*'
    return result

s1 = star(3)        # ***
s2 = star(5)        # *****
print(s1)
print(s2)



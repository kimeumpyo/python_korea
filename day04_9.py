# 세트 set = {'','',''}
# 중복이 안됨
# 중복된 값을 추가하려하면 무시

s = set({})
s2 = {'a','c','e'}

# 추가 add (규칙없이 저장된다.)
s.add('a')
s.add('b')
s.add('a')
s.add('c')
s.add('d')

# 빼기 remove
s.remove('d')

# set(중복X)
print(s)
print(s2)


# 교집합 (set 중 일치하는 값만)
s_kyo = s & s2
print(s_kyo)

# 합집합
s_sum = s | s2
print(s_sum)

# 차집합 (s에만 있고 s2에는 없는 것)
s_sub = s - s2
print(s_sub)


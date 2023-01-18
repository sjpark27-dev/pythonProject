'''
파일명 : Ex02-9-mutable_immutable.py
mutable - 메모리 값을 변경 가능 객체
      리스트(list), 세트(set), 딕셔너리(dict)
'''
me = [1,2,3]
print(id(me)) # 3187227950656
me.append(4)
print(id(me)) # 3187227950656

'''
immutable - 메모리 값 변경 불가
       정수(int), 실수(float), 문자열(str), 튜플(tuple)
'''
me = 10
print(id(me)) #
me +=1 # me = me + 1

# 튜플 테스트

# 튜플값 변경 방법(억까)
thistuple = ("피카츄", "라이츄", "파이리")
thiscast = list(thistuple)  # casting / 형변환
thiscast[1] = "잠만보"
thistuple = tuple(thiscast)
print(thistuple)
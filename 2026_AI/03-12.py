print("Hello World!") # System.out.println("Hello World!");

a = 3
i = 0

# 조건문
if a > 1:
    print("a는 1보다 큽니다.")

# 반복문
for a in [1, 2, 3]:
    print(a) # 123

# While
while i < 3:
    i += 1
    print(i) # 123

# 함수
def add(a,b):
    return a + b

add(3,4) # 7

# 길이 반환

len("012301230123012031230")

# 여러 줄을 쓰고 싶을 때 \n 보단 이게 나음
multiline="""
... Life is too short
... You need python
... 
"""

print(multiline)

# 슬라이싱에서 a[-1] 을 사용하면 맨 뒤에서 1번째 문자를 출력함

a = "1239123123123"
print(a[-2]) # 2

print(a[0:4]) # 1239

print(a[4:]) # 123123123

# 문자열 포매팅
# %s	문자열(String)
# %c	문자 1개(character)
# %d	정수(Integer)
# %f	부동소수(floating-point)
# %o	8진수
# %x	16진수
# %%	Literal % (문자 % 자체)

print("I eat %s apples." % "five")
# 'I eat five apples.'

number = 3
print("I eat %d apples." % number)
# 'I eat 3 apples.'

number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number, day))
# 'I ate 10 apples. so I was sick for three days.'

print("%10s" % "hi")
# '        hi' 오른쪽 정렬

print("%-10s" % "hi")
# 'hi        ' 왼쪽 정렬

print("%0.4f" % 3.42134234)
# '3.4213' 소숫점 4번째 까지

print("%10.4f" % 3.42134234)
# '    3.4213' 왼쪽 정렬과 소숫점 표시 

# format 을 사용한 포매팅

print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))
# 'I ate 10 apples. so I was sick for 3 days.' 이름 없이도 가능 {} 사용함

print("{0:<10}".format("hi"))
# 'hi        ' 
# 왼쪽 정렬 :< 오른쪽 정렬 :> 가운데 정렬 :^
# :=^ == 공백을 "="로 채우고 가운데 정렬
# 소숫점은 같음 {0:0.4f}
# and 표현은 {{ and }}

# f 표현법 format 을 뒤에서 빼고 f만 앞에 붙이면 됨
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
# '나의 이름은 홍길동입니다. 나이는 30입니다.'

a = "hobby"
a.count('b')
# 2 count

a = "Python is the best choice"
a.find('b')
# 14 find
a.find('k')
# -1 find

a = "Life is too short"
a.index('t')
# 8 index = find
a.index('k')
# error k is not found

",".join('a,b,c,d')
# 'a,b,c,d'

# upper lower 대문자 소문자
# lstrip rstrip strip 공백 지우기
# replace split 문자열 바꾸기 나누기 

# replace
a = "Life is too short"
a.replace("Life", "Your leg")
'Your leg is too short'

# split
a = "Life is too short"
a.split()
['Life', 'is', 'too', 'short']
b = "a:b:c:d"
b.split(':')
['a', 'b', 'c', 'd']


# isalpha isdigit startswith endswith 알파벳인지, 숫자인지, 특정 문자(열)로 시작하는지 , ~끝나는지

# startswitch
s = "Life is too short"
s.startswith("Life")
# True
s.startswith("short")
# False


# 한줄평 
# C, C++ 배워두면 좋음
#REPL Read-Eval-Print Loop 입력 받아 평가하고 출력하고 입력 받는 과정 반복
# x ** y = x의 y 제곱 값을 반환함 ex) 3 ** 4 == 81
# x // y = x와 y의 나머지 몫을 정수로 반환함 ex) 7 // 4 == 1
# 모든 내용은 "점프 투 파이썬" 책과 같음


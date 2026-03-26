# 정수,실수 나눗셈

9 / 9 # 1.0 정수
9 // 9 # 1 실수

a = (a + 1) % 5 # 0~5 순환용

# list 중요 함수
del a[1] # 삭제
len(a) # 길이 확인
a.append(4) # 리스트의 맨 마지막에 파라미터를 추가하는 함수
a.sort() # 정렬 파라미터 X
a.reverse() # 리스트 뒤집기
a.index(3) # 파라미터 값의 인덱스 반환
a.insert(0, 4) # 요소 삽입 파라미터 (위치, 값)
a.remove(3) # 요소 제거 파라미터 (값) *중복되면 첫번째 꺼*
a.pop() # 맨 마지막 요소 반환 및 제거 파라미터 X
a.count(3) # 리스트 안에 (파라미터 값)이 몇개 있는지 조사
a.extend([4,5]) # 리스트 확장 a += [4, 5] 와 동일

# 리스트는 [], 튜플은 ()으로 둘러싼다.
# 리스트는 요솟값의 생성, 삭제, 수정이 가능하지만, 튜플은 요솟값을 바꿀 수 없다.

# 딕셔너리 {Key : Value}

a['name'] = 'pey' # 추가
del a['name'] # 삭제 [Key]

a['name'] # 'pey'

a = {[1,2] : 'hi'} # error Key에 리스트 X

# 딕셔너리 중요 함수

# Key 리스트 만들기 keys
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
a.keys() # dict_keys(['name', 'phone', 'birth']) 반환

# Value 리스트 만들기 values
a.values() # dict_values(['pey', '010-9999-1234', '1118']) 반환

# Key, Value 쌍 얻기 items
a.items()
# dict_items([('name', 'pey'), ('phone', '010-9999-1234'), ('birth', '1118')])

# Key: Value 모두 지우기 clear
a.clear() # {}

# Key로 Value 얻기 get
a.get('name') # 'pey'

# key가 딕셔너리 안에 있는지 조사 in
'name' in a # True

# key로 value 얻기 pop
a = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
phone = a.pop('phone')
phone
'010-9999-1234'
# a
# {'name': 'pey', 'birth': '1118'}

# 변수

a = [1,2,3]
b = a # 리스트 복사 X
b = a[:] # 복사 O


# 제어문
# 비교 연산자 > < = !=
# 논리 연산자 and or not
# in not in (리스트, 튜플)

# else = elif

# match-case 문

grade = 'B'
match grade:
    case 'A':
        print("")
    case 'B':
        print("")
    case _: # else
        print("")
# case "A" | "B": 사용 가능

# 조건부 표현식
# 변수 = 참일 때 값 if 조건 else 거짓일 때 값
age = 19
status = "성인" if age >= 18 else "미성년"
print(status)
# 성인

# 구구단

for i in range(2,10):
    for j in range(1,10):
        print(i, "*", j, "=", i*j)


for i in range(2,10):        # 1번 for문
    for j in range(1, 10):   # 2번 for문
        print(f'{i} X {j} {i*j}, end=" "') 
    print('') 


dan = int(input())

for j in range(1, 10):
    print(f"{dan} X {j} = {dan*j}")

# 리스트 컴프리헨션
a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)
# [6, 12]

# enumerate 함수
fruits = ['apple', 'banana', 'orange']
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# 0: apple
# 1: banana
# 2: orange

# zip 함수 여러 리스트 순회
names = ['홍길동', '김철수', '이영희']
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}점")

# 홍길동: 85점
# 김철수: 92점
# 이영희: 78점

# 별 찍기
for i in range(5):
    for j in range(i):
        print("*", end='')
    print()

# *
# **
# ***
# ****
# *****

# 중앙 정렬
for i in range(1, 6):
    print(" " * (5 - i) + "*" * (2 * i - 1))

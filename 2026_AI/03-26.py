1 in [1,2,3]
# True

# else if -> elif

# 변수 = 참일_때_값 if 조건 else 거짓일_때_값

score = 85
result = "합격" if score >= 60 else "불합격"
print(result)
# 합격

# while

treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")

# continue 아래 무시하고 위로 올라감
# continue 문은 가장 가까운 while 문에만 적용

# 홀수만
a = 0
while a < 10:
    a += 1
    if a % 2 == 0: continue
    print(a)

# for

# 리스트를 할 때 i는 1부터 시작이 아닌 as2[0] 값
as2 = [2,4,1,3,5]

for i in as2:
    print(i) # 2 4 1 3 5
    
# 리스트 컴프리헨션
b3 = [1,2,3,4]
result = []
for num in b3:
    result.append(num*3)
print(result)

# result2 = [num*3 for num in b3]
# print(result) 

# [3, 6, 9, 12]



# enumerate 함수

# >>> fruits = ['apple', 'banana', 'orange']
# >>> for i, fruit in enumerate(fruits):
# ...     print(f"{i}: {fruit}")
# ...
# 0: apple
# 1: banana
# 2: orange


# 함수

def add(a, b):
    return a + b

c = add(3,2)
# c = 5

def add_many(*args): # 입력값 무한
    result = 0 
    for i in args: 
        result = result + i   # *args에 입력받은 모든 값을 더한다.
    return result 

# key : value 함수 kwargs

def print_kwargs(**kwargs):
    print(kwargs)

# >>> print_kwargs(a=1)
# {'a': 1}
# >>> print_kwargs(name='foo', age=3)
# {'name': 'foo', 'age': 3}
# >>> print_kwargs(name='홍길동', age=25, city='서울', job='개발자')
# {'name': '홍길동', 'age': 25, 'city': '서울', 'job': '개발자'}

# 응용

def create_profile(**info):
    print("=== 프로필 정보 ===")
    for key, value in info.items():
        print(f"{key}: {value}")
create_profile(이름='김철수', 나이=30, 직업='프로그래머', 취미='독서')
# === 프로필 정보 ===
# 이름: 김철수
# 나이: 30
# 직업: 프로그래머
# 취미: 독서

# return 이 2개 이상이면 튜플로 변환됨
def add_and_mul(a,b): 
    return a+b, a*b
result = add_and_mul(3,4) 
# result = (7, 12)

# lambda 예약어 def == lambda
add = lambda a, b: a+b
result = add(3, 4)
print(result)
# 7






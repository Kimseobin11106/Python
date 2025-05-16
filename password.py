# 패스워드를 검사하자. 비번이 맞을 때 까지 반복


pw = '1234'  # 문자 1234
my = input('패스워드를 입력하세요')

# 비번이 틀렸을 때 반복   pw  my 같지 않을때
while pw != my:  # !는 부정의 의미
    my = input('패스워드를 입력하세요')

print('welcome')

# pw = '1234'

# 무조건 반복하다가 조건이 맞으면 탈출(break)
# 파이썬에는 do-while문이 없음...
# True는 참을 뜻함  False은 거짓 => 대소문자 주의

# while True:
#     my = input('비번입력')
#     if my == pw:
#         break

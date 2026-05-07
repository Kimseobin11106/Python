# 한 줄 문자열을 입력받아 정수면 그대로, 아니면 메시지 출력
s = input()
try:
    n = int(s)
    print("정수")
except ValueError:
    print("숫자가 아닙니다")

# 두 정수 입력 A // B 출력 B가 0이면 메시지
line = input().split()
a = int(line[0])
b = int(line[1])
try:
    print(a // b)
    print("정수")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
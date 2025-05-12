import random
가위, 바위, 보 = 1, 2, 3
a = random.randint(1, 3)
for k in range(True):
    print('가위바위보')
    b = int(input())
    if a == 1 and b == 1:
        print('비겼습니다!')
    elif a == 1 and b == 2:
        print('이겼습니다!')
        break
    elif a == 1 and b == 3:
        print('졌습니다!')
    elif a == 2 and b ==1:
        print('이겼습니다!')
        break
    elif a == 2 and b ==2:
        print('비겼습니다!')
    elif a == 2 and b ==3:
        print('졌습니다!')
    elif a == 3 and b ==1:
        print('졌습니다!')
    elif a == 3 and b ==2:
        print('이겼습니다!')
        break
    elif a == 3 and b ==3:
        print('비겼습니다!')
# 숫자맞추기 게임
import random

# 무작위 숫자 선택 (1부터 100까지)
lan = int(input("~부터 입력하실건가요."))
lan2 = int(input("~까지 입력하실건가요."))
secret_number = random.randint(lan, lan2)

# 시도 횟수 초기화
attempts = 0

print(f"{lan}부터 {lan2}까지의 숫자를 맞추는 게임을 시작합니다.")

while True:
    # 플레이어로부터 숫자 입력 받기
    try:
        guess = int(input("숫자를 입력하세요: "))
    except ValueError:
        print("올바른 숫자를 입력하세요.")
        continue

    attempts += 1

    # 입력한 숫자와 비교
    if guess < secret_number:
        print("숫자가 너무 작습니다. 다시 시도하세요.")
    elif guess > secret_number:
        print("숫자가 너무 큽니다. 다시 시도하세요.")
    else:
        print(f"정답입니다! {attempts}번 시도했습니다.")
        break

print("게임 종료")
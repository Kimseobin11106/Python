
import random #랜덤 변수를 사용할때 import random 을 사용 후 실행 하기
ans = random.randint(1 , 100) #정답
for i in range(10):
  num = int(input()) #입력 문자를 숫자로 변환
  # ans랑 num 이랑 같은가
  if ans == num:
    print('정답입니다!')
    #빠져나가기 => 파이썬에서 반복문 빠져나가기
    break # 반복 중단
  #else 아래에 if를 또 쓰자니 번거러움..
  elif ans > num:
    print('UP')
  else:
    print('DOWN')
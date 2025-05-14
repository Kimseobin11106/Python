#숫자를 입력받기 기능 => n 이라고 하자
#1부터 n까지 반복 => for
#반복하면서 나오는 숫자가 짝수 인지 검사 %2 ==== 0
#합 구하기 => 합을 보관하는 변수 sum을 만들자
#sum변수를 누적해서 저장하자
import random
n = random.randint(1 , 100)
sum = 0
for i in range(1 , n+1):
  if i%2 == 0:
    sum = sum+i
print(sum)
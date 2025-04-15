# 내가 입력한 단만 출력

#반복문
i = int(input())
for k in range(1,10): #1부터 9까지 하나씩 가져와서 k 변수에 저장
    # 콜론(:) 을 찍어서 들여쓰기 = 반복하면서 할 일을 지정
    print(f'{i}*{k}={i*k}')

for i in range(2,5): # 2단부터 4단까지의 곱셈
  for k in range(1,10): #1부터 9까지 하나씩 가져와서 k 변수에 저장
    # 콜론(:) 을 찍어서 들여쓰기 = 반복하면서 할 일을 지정
    print(f'{i}*{k}={i*k}')

#for(int i=0; i < 10; i++) Java
#range(10) = 0~9 == range(0,10) == range(0,10,1) 0~10전까지 +1 step
# print(f"".end='') \t : tab | \n : 줄바꿈
for i in range(2, 20):
  print(f'{i}단')
  #1부터 10000까지 반복 출력
  #1~10000
  for k in range(1,20):
    print(f'{i} * {k} = {i*k}',end='\n')
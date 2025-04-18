#1
#2  3
#4  5 6
#7  8 9 10

n = 1

for i in range(1,6):
  for k in range(i):
    print(f'{n}', end='\t')
    n += 1
  print()

# 1 2 3 4 5 6 7
# 8 9 10 11 12 13 14
# ............... 35 teacher

# n = 1

for i in range(1,6): # 1~5 => 0~4? = 1씩 빼주기
  for k in range(1,8): # 1~7 => 0~6? = 1씩 빼주기
    # i,k를 이용하여 1~35 까지 출력
    print(f'{(i-1) * 7 + k}', end = '\t')

    # print(f'{n}', end = '\t')
    # n += 1
  print()
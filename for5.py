# n이 무조건 홀수
# 5
# 00800
# 08880
# 88888
# 08880
# 00800

import math

# a = 2.5
# print(math.ceil(a)) = 3

# b = 2.5
# print(int(2.5)) = 3

rows = int(input('줄 개수를 입력(홀수)'))
star = 1
zero = int(rows/2)
sw = 1

#7이라면 4번 반복
loop = int(rows/2) + 1

for i in range(rows):
  for k in range(zero):
    print(f'0', end='')
  for k in range(star):
    print(f'8', end='')
  for k in range(zero):
    print(f'0', end='')
  print()

  if i == loop - 1:
    sw = sw * -1
  star = star + (2 * sw) # 1 > 3
  zero = zero - (1 * sw) # 3 > 2
  # else:
  #   star -= 2
  #   zero += 1
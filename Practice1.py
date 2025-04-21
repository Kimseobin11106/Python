# 연습1
size = 5
for i in range(size):
  for k in range(size-i):
    print(f'*',end='')
  print()

# 연습2
size = int(input('줄 수'))
for i in range(size):
  for k in range(size-i-1):
    print(f' ', end='')
  for k in range(i*2+1):
    print(f'8', end='')
  print()
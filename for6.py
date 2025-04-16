# 00000
# 11111
# 22222
# 33333
# 44444

s = int(input("행번호 입력"))

for k in range(s):
  for i in range(5):
    print(f'{k}', end='')
  print()

# 00000
# -1-1-1-1-1
# 22222
# -3-3-3-3-3
# 44444

s = int(input("행번호 입력"))

for k in range(s):
  for i in range(5):
    if k % 2 != 0:
      print(f'{k*-1}', end='')
    else:
      print(f'{k}', end='')
  print()

# 00000
# -1-1-1-1-1
# 22222
# -3-3-3-3-3
# 44444

sw = 1

for k in range(5):
  for i in range(5):
    print(f'{k * sw}', end='')
  sw *= -1
  print()
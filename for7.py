# -1-1-1-1-1
# 22222
# -3-3-3-3-3
# 44444
# -5-5-5-5-5

sw = -1

for k in range(1,6):
  for i in range(5):
    print(f'{k * sw}', end='')
  sw *= -1
  print()

# 1 2 3 4 5 6 7
# 8 9 10 11 12 13 14
# ............... 35 me

n = 1
for k in range(5):
  for i in range(7):
    print(f'{n}', end=" ")
    n += 1
  print()

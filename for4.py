# 거꾸로 별 방법 1
i = int(input("행번호 입력"))
for k in range(i+1,1,-1):
  for a in range(k-i):
    print(f'*', end='')
  print('')

# 거꾸로 별 방법 2
rows = int(input('행입력'))
for i in range(rows):
  for i in range(rows-i):
    print(f'*', end='')
  print('')

# 오른쪽 정렬 별
rows = int(input('행입력'))
for i in range(rows):
  for k in range(rows-i-1): # 5 - 0 - 1 = 4
    print(f' ', end='')
  for k in range(i+1):
    print(f'*', end='')
  print('')

# 5
#   *
#  ***
# *****
#  ***
#   *
diamond = int(input('다이아 입력 : '))

if diamond % 2 == 1:
    i = 1
else :
    i = 2

for i in range(i, diamond+1, 2):
    blank = ' '*((diamond-i)//2)
    diamond = '*'*i

    print(blank,diamond,blank)

for i in range(i-2, 0, -2):
    blank = ' '*((diamond-i)//2)
    diamond = '*'*i

    print(blank,diamond,blank)
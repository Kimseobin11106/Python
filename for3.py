for i in range(4):
  for k in range(4):
    print(f'*', end='')
  print('')
#   *****
#   *****
#   *****

for i in range(1,5):
  for k in range(i):
    print(f'*', end='')
  print('')
# *
# **
# ***
# ****

#행번호 i를 입력받아 별을 출력하는 코드
i = int(input("행번호 입력"))
for k in range(i):
  for a in range(k+1):
    print(f'*', end='')
  print('')
# 행번호 입력5
# *
# * *
# * * *
# * * * *
# * * * * *
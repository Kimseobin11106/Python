import random

for j in range(1,20): # 1 ~ 9
  #2단~9단 옆으로 출력
  for i in range(2,20):
    print(f'{i} * {j} = {i*j}',end='\t')
  #엔터 한번
  print()

rows = 4 #가로줄
cols = 6 #세로줄

for i in range(rows):
  for j in range(cols):
    print(f'{i* cols + j + 1}',end='\t')
  print()

for i in range(4):
  for k in range(4):
    print(f'*', end='')
  print('')

rows = int(input("가로줄을 입력하세요."))
cols = int(input("세로줄을 입력하세요."))

# 4 * 6 24명 학생 준비

#실제 학생수가 24보다 클수도 있고, 작을 수도 있음..
#만약 24보다 크다면 어떡할래? 지금은 가정하지 않겠음..
#만약 적으면? 없는 자리를 X로 표시해서 24를 무조건 만들겠음.

student = ['고현준','곽권','김규민','김민성','김민후','김서빈','김지민','박민지','박진우','박현지','신보경','양현욱','유승찬']
#student 를 무조건 24명으로 만들어 버림(없는자리는 X로 처리)
#현재 13명 있음. 어떻게 24로 만들까? 현재가 만약 n 명이라면??
#현재가 몇명인지 알 수 있나? = len(student)
a = cols * rows - len(student)

for y in range(a):
  student.append('X')


random.shuffle(student)

cnt = 0
for k in range(rows):
  for i in range(cols):
    print(f'{student[cnt]}',end='\t')
    cnt += 1
  print()
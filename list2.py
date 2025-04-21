list = []

def pop(): # 값을 꺼낼 때 기능
  if len(list) > 0: # list의 길이를 검사
    list.pop()
  else: # 길이가 0
    print('비어있습니다.')


def push(value): # 값을 추가할 때 기능
  list.append(value)


while(True):
  print(f'현재상태 : {list}')
  select = input('동작을 입력하세요 1.삭제 2.삽입 3.종료')
  if select == '1': # 삭제
    pop()
  elif select == '2': # 삽입
    val = input('값을 입력하세요')
    push(val)
  elif select == '3': # 종료
    break
  else:
    print('1,2,3 중 다시 선택해주세요')
# 배열의 크기를 정하고, append, pop 없이 구현

global pos, size # global 을 선언을 먼저해야 함수에서 같이 사용할 수 있음
size = int(input('배열의 크기를 입력하세요.'))
list = []

pos = -1 # 아무것도 지정되지 않음

for i in range(size):
  list.append(0) # 0으로 초기화 [0,0,0....0]

def pop():
  global pos
  if pos > -1: # 하나라도 있다면 꺼내기 => 0으로 표현
    list[pos] = 0
    pos -= 1 # 위치를 하나 아래로 설정
  else:
    print('값이 없습니다.')

def push(value):
  global pos
  if pos >= size - 1: # 마지막 상황에서 9 >= 10 - 1
    print('배열이 가득 찼습니다.')
  else:
    pos += 1
    list[pos] = value

def show():
  global pos
  for i in range(pos+1):
    print(f'{list[i]}', end='\t')

while(True):
  print(f'pos : {pos}')
  sel = input('동작을 입력하세요 1.pop 2.push 3.show')
  if sel == '1':
    pop()
  elif sel == '2':
    val = input('값을 입력하세요')
    push(val)
  elif sel == '3':
    show()
  else:
    print('다시 선택해주세요')
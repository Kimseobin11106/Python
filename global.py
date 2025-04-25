arr = [
    [1,1,0,0],
    [0,1,1,0],
    [0,1,0,0],
    [0,1,1,1]
      ]

def start(x, y):
  #오른쪽확인
  #아래쪽확인
  global arr # arr을 전역 변수로 선언
  print(arr[x,y])

start(0,0)
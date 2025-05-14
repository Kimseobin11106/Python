# 가위=1 바위=2 보=3 게임
me = int(input('나는 뭐 낼래? 가위1 바위2 보3'))
com = int(input('컴퓨터는 뭐 낼래? 가위1 바위2 보3'))
if me == com:
  print('비김')
#내가 이기는 경우
#나 1 - 3 컴
#나 2 - 1 컴
#나 3 - 2 컴

elif (me == 1 and com == 3) or (me == 2 and com == 1) or (me == 3 and com == 2): # (me-com) % 3 == 1:
  print('이기심')
else:
  print('지심')
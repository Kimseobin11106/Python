#리스트와 for를 사용해보자.
#리스트를 만드는데 [0,1,2,3,4] 가 보관된 리스트 만들기
lt = [] # 아무것도 없는 리스트 .append 를 이용해 추가
size = int(input("크기를 입력하세요"))
for i in range(0 , size+1):
  # 들여쓰기 조심
  lt.append(i)
print(lt)
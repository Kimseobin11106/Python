#[0 , 10 , 20 , 30 , 40 ... 1000] 인 배열 만들자.
lt = []
#for 변수 in 범위(리스트를 써도 되고 , range()이용 )
for i in range(0 , 1001 , 10):
  lt.append(i)
print(lt)

#리스트에서 index를 쓰지 않고 해당 위치 변환

a = [1,2,3,4,4,4,7]  #크기고정
size = len(a)  #a 배열의 길이  ,  a.length 아님(자바에서 이렇게)...
find = 5

#for문을 이용  => a의 크기 만큼 반복검사
for k in range(size):
  #a[k]야 find를 같음?
  if a[k] == find:
    print(k)
    break



#a에서 쓸수 있는 기능
#pos = a.index(4)  #4의 위치는?
#print(pos)


###결과###
# 4입력 =>   3(번지)출력

str = 'hello world' #문자열도 리스트로 다룰 수 있음
print(str[6])
print(str.index('w'))
#문자열에서는 find 명령어도 사용할 수 있음
print(str.find('w'))
#find는 찾지 못하면 오류대신 -1을 출력
print(str.find('T'))  
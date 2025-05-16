
#마지막부터 값 찾기
#hint  range의 활용

a = [0,1,2,3,4,5,6,7,8,9]
size = len(a)
find = int(input())
#range(5) 0~4까지
#range(1,5) 1~4까지
#range(1,10, 2)  1~9까지 2씩 증가
#10부터 1까지 1씩 감소 =>  range(11, 0, -1)
# for k in range(size-1, -1 , -1):
#   if a[k] == find:
#     print(k)
#     break


for k in range(size):
  #0 번지 => 9만들기
  pos = size - 1 - k  #k=0일때 10-1-k=>9-0 = 9번지 찾기
  if a[pos] == find:
    print(pos)
    break
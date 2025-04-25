# 재귀 호출 | 1~10까지 출력 단 반복문을 이용하지 않고 풀기
def jump(num):
  print(num)
  if num < 10:
    jump(num+1)

jump(1)

# factorial n!
# 재귀호출 : 내가 나를 부르는 호출방법
#            이전 단계가 다 끝나야 내가 끝날 수 있음
def fact(n):
  if n == 1:
    return 1
  else:
    return n * fact(n-1)

print(fact(5))
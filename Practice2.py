# 수행평가 소수 판별 = 1과 자신을 제외한 수 중에 나누어지지 않는 수(단, 2이상)

number = int(input('숫자입력'))

for n in range(2, number+1):
  is_prime = True
  for k in range(2, n):
    if n % k == 0:
      print('소수가 아닙니다')
      is_prime = False
      break;

  if is_prime == True:
    print(n)
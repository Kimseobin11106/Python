# del sum 함수 삭제 : 미리 정해진 함수의 이름을 변수로 지정했을 때 오류가 발생하는 것을 막기위한 코드

arr = [2,-34,42,-41,45,-43,-52,50,-53]

start = 0
end = 3
total = 0

for i in range(start,end+1):
  total += list[i] # 기존의 값에 새로운 값을 계속 누적하여 더함

print(total)

print(  sum(list[start :  end+1]) ) #sum (항목 부터 항목까지의 값을 더함)
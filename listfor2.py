# 연속된 범위를 선택했을 때 최대합은 얼마일까?
arr = [2,-34,42,-41,45,-43,-52,50,-53]

total = -999999999999

for k in range(len(list)):
  for a in range(k, len(list)):
      total = max(total, sum(list[k : a+1])) #max (엑셀과 같음, 항목 중 최대값 반환)

print(total)
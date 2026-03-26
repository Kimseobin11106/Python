n, m = map(int, input().split())

basket = list(range(1, n+1)) # [1,2,3,...,n] 생성

for _ in range(m):
    i, j = map(int, input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1] # swap

print(*basket) # 리스트 공백 출력
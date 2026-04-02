n, m = map(int, input().split())

basket = [0] * n # 0으로 초기화

for _ in range(m):
    i, j, k = map(int, input().split())
    
    for x in range(i-1, j):
        basket[x] = k

print(*basket) # 리스트 공백
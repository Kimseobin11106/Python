a = [list(map(int, input().split())) for _ in range(9)]

max_val = a[0][0]
row = 0
col = 0

for i in range(9):
    for j in range(9):
        if max_val < a[i][j]:
            max_val = a[i][j]
            row = i
            col = j

print(max_val)
print(f"{row+1} {col+1}")
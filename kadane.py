# 최대합 (kadane 알고리즘)
arr = [2, -34, 65, -7, 1 ,34, -31, 32]

print(arr)
for k in range(1, len(arr)):
    arr[k] = max(arr[k],  arr[k] + arr[k-1])
    print(arr)

print(f'result : {arr[7]}')
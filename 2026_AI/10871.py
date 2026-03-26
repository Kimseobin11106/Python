# 배열 X보다 작은 수

# best
n, x = map(int, input().split())
a = list(map(int, input().split()))

for i in a:
    if i < x:
        print(i, end=" ")


# n,x = map(int, input().split())

# a = list(map(int, input().split()))

# ans = []

# for i in range(0, len(a)):
#     if a[i] < x:
#         ans.append(a[i])

# for i in range(0, len(ans)):
#     print(ans[i] ,end=" ")
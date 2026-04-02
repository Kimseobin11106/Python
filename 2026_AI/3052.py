s = set() # 중복 노 허용 집합

for _ in range(10):
    n = int(input())
    s.add(n % 42)

print(len(s))

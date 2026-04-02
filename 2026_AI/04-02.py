treeHit = 0
while treeHit < 10:
    treeHit += 1
    print(f"나무를 {treeHit}번 찍었습니다.")
    if treeHit == 10:
        print("나무 넘어갑니다.")

p = """
    1. Add
    2. Del
    3. List
    4. Quit
"""
n = 0
while n != 4:
    print(p)
    n = int(input())

a = 0
while a < 10:
    a+=1
    if a % 2 == 0: continue
    print(a)

def add(a,b):
    print(f"{a}, {b}의 합은 {a+b}입니다.")
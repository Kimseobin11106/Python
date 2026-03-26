t = int(input())

for _ in range(t):
    C = int(input())
    
    c500 = C // 500
    C %= 500
    
    c100 = C // 100
    C %= 100
    
    c50 = C // 50
    C %= 50
    
    c10 = C // 10
    
    print(c500, c100, c50, c10)
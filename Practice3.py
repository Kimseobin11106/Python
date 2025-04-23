# 수행평가 3 6 9 박수
n = int(input())

for number in  range(1,n+1):
    is_jjak = False
    i = number
    while(number > 0):
        d = number % 10
        if d == 3 or d == 6 or d == 9:
            print('짝!')
            is_jjak = True
            break
        number = int(number / 10 )
    if is_jjak == False:
        print(i)

# n = int(input())
# 
# for i in range(1, n+1):
#   if str(i).count('3') == 1 or str(i).count('6') == 1 or str(i).count('9') == 1:
#     print("짝")
#   else:
#     print(i)
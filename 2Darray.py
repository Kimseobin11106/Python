# 2차원 배열
arr = [1,2,3]
list = [arr, arr, arr] # [ [1,2,3] [1,2,3] [1,2,3] ]
# call by reference 참조에 의한 호출을 사용 (관계)
print(list)

arr.append(4) #arr [1,2,3,4]
print(list) # [ [1,2,3,4] [1,2,3,4] [1,2,3,4]]

# 참조에 의한 호출이기 때문에 list의 값도 같이 변경이 됨
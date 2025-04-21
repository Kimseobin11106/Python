# 파이썬 배열 == 리스트
# list = [] # 공백
# list = [1,2,3,4]
list2 = ['a',1,2,3] # 다른 자료형도 사용 가능
list2.append(4) # append 이용하여 마지막 항목 추가
list2.remove('a') # remove는 항목을 검색해서 삭제


list2.append(1) # [1,2,3,4,1]
print(list2)
list2.remove(1) # 누가 삭제 될까? => 앞에 있는 값이 삭제
print(list2) # [2,3,4,1]

list2.pop() # 항상 마지막 항이 삭제
print(list2) # [2,3,4]

list2.insert(1, 5) # 1번지에 5를 넣어라
print(list2) # [2,5,3,4]

# [3][3]
list = [
    [1,2],
    [4,5,6],
    [7,8]
]
print(list[2][1])


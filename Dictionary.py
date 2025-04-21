# 딕셔너리
studentA = [100,80,80,90] # 과목 1234
studentB = {
            'korean':100,
            'math':80,
            'eng': 80,
            'info':90
            } # 딕셔너리 타입 Dictionary : 'Key' : 'Value'의 조합으로 이루어짐
print(studentA[0])
print(studentB['korean'])

#B학생에게 jpn 성적 100점 추가
studentA.append(100)
studentB['jpn'] = 100
print(studentB)


flag = False # 과학찾기
# print(studentB.keys())
# print(*studentB.keys())
for k in studentB.values():
  if (k == "sci"):
    flag = True
if flag == True:
  print("과학있음")
else:
  print("과학없음")

if 'sci' in studentB: # key 검사
  print('과학 진짜 있음')
else:
  print('과학 진짜 없음')
#파이썬에서는 함수를 def라고 선언, 중괄호가 없음(들여쓰기와 콜론(:)으로 구별)

def go(step):
  if step > 10:
    return
  print(step)
  go(step+1)


go(1)
import my_stack as st
# stack1 = st.MyStack(size=5)
# stack2 = st.MyStack(size=10)

stack = [st.MyStack(size=5), st.MyStack(size=10)]
st2 = st.MyStack(size=12)

while True:
    action = input('동작을 입력하세요. 1번조작, 2번조작, q나가기')
    if action == 'q':
        break
    else: #1, 2를 눌렀으면
        target = int(action) - 1 # 1번 = 0, 2번 = 1
        act = input('1.push, 2.pop, 3.view')
        if act == '1':
            val = input('값을 입력하세요')
            if stack[target].push(value=val) == True:
                print('성공')
        elif act == '2':
            print()
        elif act == '3':
            print()

print(stack[0].view())
print(stack[1].view())
print(st2[1].view())
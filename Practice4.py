# 문제 1134번

target = input("찾을 글자를 입력하세요")  # KTX
src = input("문자열을 입력하세요")  # KINTEX
t_pos = 0
for s in src:
    # KINTEX의 K == KTX[0]인 K 같은지 비교
    if s == target[t_pos]:
        # 만약 글자를 찾으면 target의 다음 글자
        t_pos = t_pos + 1

        if len(target) == t_pos:
            print('Y')
            break
        else:
            print('N')

print('끝')
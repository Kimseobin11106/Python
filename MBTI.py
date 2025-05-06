#MBTI 성격검사
def mbti_test():
    questions = [
        "1. 당신은 대체로 어떤 사람입니까?\nA. 외향적인 사람\nB. 내향적인 사람",
        "2. 다음 중 어떤 것이 더 중요한가요?\nA. 감정\nB. 이성",
        "3. 어떤 활동을 더 선호하십니까?\nA. 계획을 세우는 것\nB. 순발력 있는 대응",
    ]

    mbti_types = {
        'ISTJ': 0, 'ISFJ': 0, 'ESTJ': 0, 'ESFJ': 0,
        'ISTP': 0, 'ISFP': 0, 'ESTP': 0, 'ESFP': 0,
        'INTJ': 0, 'INFJ': 0, 'ENTJ': 0, 'ENFJ': 0,
        'INTP': 0, 'INFP': 0, 'ENTP': 0, 'ENFP': 0,
    }

    print("MBTI 테스트를 시작합니다. 각 질문에 대해 A 또는 B 중 하나를 선택해주세요.")

    for question in questions:
        answer = input(question + "\n답변 (A/B): ").strip().upper()
        while answer not in ['A', 'B']:
            print("유효한 답변이 아닙니다. 다시 입력해주세요.")
            answer = input("답변 (A/B): ").strip().upper()

        for mbti_type in mbti_types:
            if answer == 'A':
                mbti_types[mbti_type] += 1
            else:
                mbti_types[mbti_type] -= 1
    max_mbti_type = max(mbti_types, key=mbti_types.get)

    print(f"당신의 MBTI 유형은 {max_mbti_type} 입니다.")

if __name__ == "__main__":
    mbti_test()
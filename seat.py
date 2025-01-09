import random

# 참가자 정보
participants = {
    "장재혁": {"공부법": "국어", "진로": "진로3", "기타": "기타3"},
    "최준환": {"공부법": "국어", "진로": "학과박람회", "기타": "아브"},
    "이유경": {"공부법": "국어", "진로": "진로1", "기타": "기타3"},
    "김지윤": {"공부법": "국어", "진로": "진로1", "기타": "아브"},
    "이태림": {"공부법": "수학", "진로": "진로3", "기타": "기타2"},
    "임재현": {"공부법": "수학", "진로": "비교과", "기타": "운동회"},
    "조서영": {"공부법": "영어", "진로": "진로2", "기타": "운동회"},
    "정근규": {"공부법": "과탐", "진로": "진로1", "기타": "기타1"},
    "조주형": {"공부법": "과탐", "진로": "시간관리", "기타": "레크리에이션"},
    "하수진": {"공부법": "사탐", "진로": "학과박람회", "기타": "아브"},
    "민주은": {"공부법": "사탐", "진로": "면접", "기타": "아브"},
    "전지훈": {"공부법": "사탐", "진로": "진로3", "기타": "기타1"},
    "김지정": {"공부법": "사탐", "진로": "진로2", "기타": "기타2"},
    "임서연": {"공부법": "영어", "진로": "비교과", "기타": "기타3"},
    "오승훈": {"공부법": "과탐", "진로": "비교과", "기타": "운동회"},
    "이주형": {"공부법": "수학", "진로": "진로2", "기타": "기타2"}
}

# 자리배치표 생성 함수
def generate_seating_chart(names):
    rows, cols = 8, 2
    seating_chart = [[None for _ in range(cols)] for _ in range(rows)]
    attempts = 0

    while attempts < 1000:  # 최대 1000번 시도
        random.shuffle(names)  # 참가자 무작위 섞기
        filled = True
        remaining_names = names[:]  # 원본 리스트 복사

        for i in range(rows):
            for j in range(cols):
                valid_names = [name for name in remaining_names if is_valid(name, seating_chart, i, j)]
                if valid_names:
                    chosen_name = valid_names[0]
                    seating_chart[i][j] = chosen_name
                    remaining_names.remove(chosen_name)
                else:
                    filled = False
                    break
            if not filled:
                break

        if filled:
            return seating_chart
        else:
            # 실패 시 재시도
            remaining_names = names[:]
            seating_chart = [[None for _ in range(cols)] for _ in range(rows)]
            attempts += 1

    raise ValueError("자리 배치 실패: 규칙을 만족하는 배치를 찾을 수 없습니다.")

# 자리 유효성 검사 함수
def is_valid(name, seating_chart, row, col):
    person = participants[name]

    # 인접한 자리 확인
    adjacent_positions = [
        (row - 1, col), (row + 1, col),  # 위아래
        (row, col - 1), (row, col + 1)   # 좌우
    ]
    for r, c in adjacent_positions:
        if 0 <= r < 8 and 0 <= c < 2:  # 유효한 좌표만 검사
            neighbor = seating_chart[r][c]
            if neighbor and (
                person["공부법"] == participants[neighbor]["공부법"] or
                person["진로"] == participants[neighbor]["진로"] or
                person["기타"] == participants[neighbor]["기타"]
            ):
                return False
    return True

# 참가자 리스트
names = list(participants.keys())

# 자리배치표 생성 및 출력
try:
    seating_chart = generate_seating_chart(names)

    print("자리배치표:")
    for row in seating_chart:
        print(row)
except ValueError as e:
    print(e)



while True:
    try:
        print(participants[input().strip()])
    except:
        continue
    
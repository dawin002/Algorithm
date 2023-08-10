""" 18870 : 좌표 압축 """

# n 개 좌표 (x축상)
# 그 순서대로 n 개 좌표 값 대소 안바뀌게 0 이상의 정수로 압축
# 순서 그대로 압축된 좌표 출력

""" my solution : 시간 초과, 힌트 써서 통과 """

def zip_x():
    import sys
    input = sys.stdin.readline
    input()
    ori = list(map(int, input().split()))
    new = sorted(list(set(ori)))

    # 딕셔너리 써야 통과 가능
    dict = {}  # 딕셔너리 생성
    idx = 0
    for i in new:
        dict[i] = idx  # 딕셔너리에 원소 추가
        idx += 1

    # 원래 순서대로 딕셔너리에서 검색해 압축 순서 출력
    for i in range(len(ori)):
        ori[i] = dict[ori[i]]

    print(' '.join(map(str, ori)))

zip_x()

""" my solution"""
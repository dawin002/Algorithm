""" 2851 - 슈퍼 마리오 """

# 10개의 점수가 다른 버섯 일렬로 주어짐
# (각 버섯 1 <= 점수 <= 100)
# 처음부터 순서대로 집어야함
# 중간에 건너뛰기 안됨
# 100에 최대한 가까운 점수 뽑기
# 98, 102 두 점수 가능하면 더 큰 점수로

""" my solution """

def super_mario():
    arr = [int(input()) for _ in range(10)]
    max_s = 0
    score = 0
    for a in arr:
        score += a
        if abs(100 - score) <= abs(100 - max_s):
            max_s = score
        else:
            break
    print(max_s)
super_mario()


""" answer solution """

# 배열 안써도 됨

def super_mario_f():
    ms = 0
    ns = 0
    for _ in range(10):
        now = int(input())
        ns += now
        if abs(100-ns) <= abs(100-ms):
            ms = ns
        else:
            break
    print(ms)
super_mario_f()
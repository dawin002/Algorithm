""" 14931 : 물수제비 """

# 1 ~ L번 칸, 1 <= L <= 1백만
# 각 칸 점수 다름
# 일정한 정수 칸마다 방문 가능
# 최대 점수 받을 수 있는 간격 d와 최대값 출력

""" my solution """

# L 범위 내의 소수 리스트 구하기
# -> 리스트의 소수 간격씩 뛰어넘게 L 리스트 슬라이싱
# -> 슬라이싱한 리스트에서 소수의 배수 중 L 범위 내의 배수들 간격씩 뛰어넘게
#    소수, 소수의 배수들 별 max 값 구해 간격별 합계 리스트에 저장
# -> 간격별 합계 리스트의 최대값, 최대값의 인덱스 출력

"""
    소수 이용해서 연산 회수 줄어보려 해서 성공했지만 너무 복잡함
    사실 그냥 완탐해도 풀리는 문제였음 
"""

def water_stone():
    INF = -int(1e9)
    n = int(input())    # 30
    arr = list(map(int, input().split()))
    d_lst = [INF] * (n+1)

    prime = [False, True, True] + [True, False] * (n-1//2)
    for i in range(3, n//2+1):
        if prime[i]:
            j = 3
            while i*j <= n:
                prime[i*j] = False
                j += 1

    p_lst = []
    for i in range(1, n+1):
        if prime[i]:
            p_lst.append(i)

    d_lst[1] = sum(arr)
    for i in p_lst[1:]:
        tmp_lst = arr[i-1::i]
        for j in range(1, n//i+1):
            # print(i, j, tmp_lst[j-1::j])
            if d_lst[i*j] == INF:
                d_lst[i*j] = sum(tmp_lst[j-1::j])

    ### test
    # print(d_lst)

    max_val = max(d_lst)
    max_idx = d_lst.index(max_val)

    if max_val <= 0:
        max_idx, max_val = 0, 0

    print(max_idx, max_val)

# water_stone()


""" answer solution : 그냥 완전탐색 """

def water_stone_ans():
    L = int(input())
    scores = list(map(int, input().split()))

    max_val, max_idx = 0, 0
    for i in range(0, L):
        sum_val = 0
        index = i + 1
        for j in range(i, L, index):
            sum_val += scores[j]
        if sum_val > max_val:
            max_val = sum_val
            max_idx = index
    print(max_idx, max_val)


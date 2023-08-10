# n명 사람 일렬로 서있음
# 각 사람 위치 + 특정 수 로 편지 보냄
# 서로 편지 주고받은 사람 쌍의 개수 구히기
# n <= 200, k 절대값 <= 200

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        arr[i] = i + arr[i]
    count = 0
    for i in range(n):
        if 0 <= arr[i] < n and arr[arr[i]] == i and arr[i] != i:
            count += 1
    print(f"#{tc}", count//2)


# 10
# 2
# 1 -1
# 3
# 2 1 -2
# 4
# 3 1 -1 -3
# 5
# 1 -1 -4 -2 -2
# 6
# 3 4 -1 1 -2 -4
# 7
# 1 -1 1 -1 1 -1 1
# 10
# -7 7 4 -6 -3 2 -1 -2 -7 2
# 11
# -3 6 7 4 -4 1 5 -8 -9 -7 -6
# 12
# 5 1 -1 4 2 -5 -3 -4 -3 2 -3 1
# 13
# 1 -9 8 2 -2 5 2 2 -2 1 -1 -8 -1
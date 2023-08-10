""" 10810 : 공 넣기 """

# n 개 바구니 (1~n 번)
# 1~n번 공 종류, 무한개
# 각 바구니 공 1개씩 넣을 수 있음
# m 번 공을 넣음
# 한번 공을 넣을때 공 넣을 바구니 범위 정하고 모두 같은 번호의 공 넣음
# 바구니에 공 있으면 빼고 지금 공 넣음

# 입력 1줄: n, m
# 입력 m줄: i, j, k (i~j 바구니 k번 공으로 채움)
# 출력 : 각 바구니에 든 공 수

n, m = map(int, input().split())
arr = [0] * (n+1)
for _ in range(m):
    i, j, k = map(int, input().split())
    for l in range(i, j+1):
        arr[l] = k
print(' '.join(map(str, arr[1:])))
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1 for _ in range(m)] for _ in range(n)]
dp[-1][-1] = 1


def recur(x, y, pre_val):
    if arr[x][y] >= pre_val:
        return 0

    if dp[x][y] != -1:
        return dp[x][y]

    tmp = 0
    for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            tmp += recur(nx, ny, arr[x][y])
    dp[x][y] = tmp
    return dp[x][y]


recur(0, 0, 999999999)

print(dp[0][0])

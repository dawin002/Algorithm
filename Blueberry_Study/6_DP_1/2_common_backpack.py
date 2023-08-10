n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
INF = int(1e9)
dp = [[-1 for _ in range(k+1)] for _ in range(n)]

def recur(idx, weight):
    if weight > k:
        return -INF

    if idx == n:
        return 0

    if dp[idx][weight] != -1:
        return dp[idx][weight]

    w, h = arr[idx]
    dp[idx][weight] = max(recur(idx + 1, weight + w) + h, recur(idx + 1, weight))

    return dp[idx][weight]

recur(0, 0)


print(max(dp[0]))
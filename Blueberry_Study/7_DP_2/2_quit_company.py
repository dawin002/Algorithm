import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n+1)]
for date in range(n)[::-1]:
    if date + arr[date][0] > n:
        dp[date] = dp[date+1]
    else:
        dp[date] = max(arr[date][1] + dp[date + arr[date][0]], dp[date + 1])

print(dp[0])
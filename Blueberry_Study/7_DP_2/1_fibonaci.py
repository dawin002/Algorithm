
def fibo1():
    n = int(input())
    f1 = 0
    f2 = 1
    i = 2
    while i <= n:
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        i += 1
    if n < 2:
        print(n)
    else:
        print(f3)

def fibo2():
    n = int(input())
    dp = [0 for _ in range(46)]
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-2] + dp[i-1]
    print(dp[n])
fibo2()
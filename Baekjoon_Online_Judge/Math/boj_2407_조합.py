""" 2407 : 조합 """

# 문제
# nCm을 출력한다.

# 입력
# n과 m이 주어진다. (5 ≤ n ≤ 100, 5 ≤ m ≤ 100, m ≤ n)

# 출력
# nCm을 출력한다.

#
""" my code """


# 힌트 : nCm = n! / ( m! * (n-m)! )


def factorial(a):
    if a == 1:
        return 1
    return a * factorial(a - 1)


def factorial_better(a):
    res = 1
    for i in range(2, a + 1):
        res *= i
    return res


def combinationsEx():
    n, m = map(int, input().split())
    print(factorial(n) // (factorial(m) * factorial(n - m)))


""" faster code """


def combinationsEx_b():
    n, m = map(int, input().split())
    ans = 1

    for i in range(n, n - m, -1):
        ans = int(ans * i)

    for j in range(1, m + 1):
        ans = int(ans // j)

    print(ans)

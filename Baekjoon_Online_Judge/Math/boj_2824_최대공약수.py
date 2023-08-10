""" 2824 : 최대공약수 """

# 문제
# 상근이는 학생들에게 두 양의 정수 A와 B의 최대공약수를 계산하는 문제를 내주었다.
# 그런데, 상근이는 학생들을 골탕먹이기 위해 매우 큰 A와 B를 주었다.

# 상근이는 N개의 수와 M개의 수를 주었고, N개의 수를 모두 곱하면 A, M개의 수를 모두 곱하면 B가 된다.

# 이 수가 주어졌을 때, 최대공약수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 1000)이 주어진다.
# 둘째 줄에는 N개의 양의 정수가 공백으로 구분되어 주어진다.
# 이 수는 모두 1,000,000,000보다 작고, N개의 수를 곱하면 A가 된다.
# 셋째 줄에 M(1 ≤ M ≤ 1000)이 주어진다.
# 넷째 줄에는 M개의 양의 정수가 공백으로 구분되어 주어진다.
# 이 수는 모두 1,000,000,000보다 작고, M개의 수를 곱하면 B가 된다.

# 출력
# 두 수의 최대공약수를 출력한다. 만약, 9자리보다 길다면, 마지막 9자리만 출력한다.
# (최대 공약수가 1000012028인 경우에는 000012028을 출력해야 한다)

#
""" my code """


def divisorList(lst, dlst):
    for a in lst:
        while True:
            for i in range(2, int(a ** 0.5) + 1):
                if a % i == 0:
                    dlst.append(i)
                    a //= i
                    break
            else:
                dlst.append(a)
                break
    dlst.sort()


def bigNumGCD():
    import sys
    input = sys.stdin.readline
    input()
    ln = list(map(int, input().rstrip().split()))
    input()
    lm = list(map(int, input().rstrip().split()))

    ldn = [1]
    ldm = [1]

    divisorList(ln, ldn)
    divisorList(lm, ldm)

    gcd = 1

    while True:
        print(ldn)
        print(ldm)
        if ldn[0] == ldm[0]:
            gcd *= ldn.pop(0)
            ldm.pop(0)
        elif ldn[0] < ldm[0]:
            ldn.pop(0)
        elif ldn[0] > ldm[0]:
            ldm.pop(0)
        if len(ldn) <= 0 or len(ldm) <= 0:
            break

    if gcd >= 1000000000:
        print(str(gcd)[-9:])
    else:
        print(gcd)


#
""" better code """


def bigNumGCD_b():
    import sys
    input = sys.stdin.readline
    input()
    nl = list(map(int, input().split()))
    input()
    ml = list(map(int, input().split()))

    n, m = 1, 1
    # 곱하기
    for a in nl:
        n *= a
    for a in ml:
        m *= a

    # 곱하는 방법 2
    n = eval('*'.join([str(a) for a in nl]))
    m = eval('*'.join([str(a) for a in ml]))

    # gcd
    while m > 0:
        n, m = m, n % m

    # 출력
    print(str(n)[-9:])

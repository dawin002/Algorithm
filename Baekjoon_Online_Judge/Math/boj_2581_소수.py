""" 2581 : 소수 """

# m, n 이 주어지면
# m 이상 n 이하의 자연수 중 소수들의 합과 소수 중 최소값을 구하라

""" my solution """


def prime_num():
    m = int(input())
    n = int(input())
    arr = [False, False, True] + [True, False] * (n // 2 + 1)
    i = 3
    while i < int(n ** (1 / 2)) + 1:
        if arr[i]:
            for j in range(2, n // i + 1):
                arr[i * j] = False
        i += 1

    arr2 = [a for a in range(m, n+1) if arr[a]]
    s = sum(arr2)
    if s == 0:
        print(-1)
    else:
        print(s)
        print(min(arr2))


prime_num()

""" answer code """


def prime_num_ans():
    m = int(input())
    n = int(input())
    l = [1] * (n + 1)
    l[1] = 0
    for i in range(2, int(n ** (0.5)) + 1):
        if l[i]:
            for j in range(i * i, n + 1, i):
                l[j] = 0

    l = [i for i in range(m, n + 1) if l[i] == 1]
    if sum(l) == 0:
        print(-1)
    else:
        print(sum(l))
        print(min(l))

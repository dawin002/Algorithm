def sequence_1():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    prefix = [0 for _ in range(n+1)]

    for i in range(1, n+1):
        prefix[i] = prefix[i-1] + arr[i-1]

    res = [-int(1e9) for _ in range(n+1)]

    for i in range(k, n+1):
        res[i] = prefix[i] - prefix[i-k]

    # print(arr)
    # print(prefix)
    # print(res)

    print(max(res))


def sequence_2():
    n, k = map(int, input().split())
    prefix = [0] + list(map(int, input().split()))
    maxi = -int(1e9)
    for i in range(1, n+1):
        prefix[i] = prefix[i] + prefix[i-1]
        if i >= k:
            maxi = max(maxi, prefix[i] - prefix[i-k])

    print(maxi)

sequence_2()


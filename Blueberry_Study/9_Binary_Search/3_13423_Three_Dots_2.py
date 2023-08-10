import sys
input = sys.stdin.readline

def bin_search(s, e, t):
    while s <= e:
        m = (s + e) // 2
        if arr[m] == t:
            return 1
        elif arr[m] < t:
            s = m + 1
        else:
            e = m - 1
    return 0

T = int(input())
for _ in range(T):

    n = int(input())
    arr = sorted(list(map(int, input().split())))

    count = 0

    s = 0
    e = n-1

    for a in range(0, n-1):
        for b in range(a+1, n):
            count += bin_search(0, n-1, arr[b] + (arr[b] - arr[a]))

    print(count)
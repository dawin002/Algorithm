import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):

    n = int(input())
    arr = sorted(list(map(int, input().split())))

    count = 0

    for a in range(0, n-2):
        for b in range(a+1, n-1):
            s = b+1
            e = n-1
            t = arr[b] + (arr[b] - arr[a])
            if t <= arr[-1]:
                while s <= e:
                    m = (s + e) // 2
                    if arr[m] == t:
                        count += 1
                        break
                    elif arr[m] < t:
                        s = m + 1
                    else:
                        e = m - 1

    print(count)
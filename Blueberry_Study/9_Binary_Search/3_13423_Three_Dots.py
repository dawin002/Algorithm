import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):

    n = int(input())
    arr = sorted(list(map(int, input().split())))

    count = 0
    # print(arr)
    for a in range(0, n-2):
        b = a+1
        c = a+2
        # print(arr[a])
        while a < b < c <= n - 1:
            if arr[b] - arr[a] == arr[c] - arr[b]:
                if arr[a] != arr[b] != arr[c]:
                    count += 1
                # print(arr[a], arr[b], arr[c])
                b += 1
                c += 1

            elif arr[b] - arr[a] < arr[c] - arr[b]:
                    b += 1
                    c += 1

            elif arr[b] - arr[a] > arr[c] - arr[b]:
                c += 1

    print(count)
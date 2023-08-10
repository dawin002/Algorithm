import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

s = 1
e = max(arr)
maxi = 0

while s <= e:
    mid = (s + e) // 2
    now = 0
    for i in arr:
        now += max(i - mid, 0)

    if now == m:
        maxi = max(maxi, mid)
        break

    elif now > m:
        maxi = max(maxi, mid)
        s = mid + 1

    elif now < m:
        e = mid - 1

print(maxi)

# 2 10
# 3 9
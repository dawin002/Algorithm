import sys

n = int(input())
arr = list(sys.stdin.readline().rstrip())

s = 0
e = 0
dist = 0

letters = [arr[s]]

while s < len(arr) and e < len(arr):
    dist = max(dist, e - s + 1)

    if len(letters) <= n:
        e += 1
        if e < len(arr) and arr[e] not in letters:
            letters.append(arr[e])

    elif len(letters) > n:
        s += 1
        e = s
        letters = [arr[s]]

print(dist)
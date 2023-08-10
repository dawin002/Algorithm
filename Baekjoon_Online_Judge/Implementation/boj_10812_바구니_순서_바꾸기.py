""" 10812 : 바구니 순서 바꾸기 """

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [i for i in range(n+1)]
for _ in range(m):
    i, j, k = map(int, input().split())
    tmp = arr[k:j+1] + arr[i:k]
    arr = arr[:i] + tmp + arr[j+1:]
print(*arr[1:])
""" 9506 : 약수들의 합"""

import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == -1:
        break
    arr = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            arr.append(i)
            if i != n // i:
                arr.append(n//i)
    arr = sorted(arr)[:-1]
    if sum(arr) == n:
        arr = ' + '.join(map(str, list(arr)))
        print(n, '=', arr)
    else:
        print(n, 'is NOT perfect.')

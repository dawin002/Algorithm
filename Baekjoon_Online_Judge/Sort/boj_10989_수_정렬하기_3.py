""" 10989 : 수 정렬하기 3 """

def sort_num_3():
    import sys
    input = sys.stdin.readline
    arr = [0] * 10001
    n = int(input())
    for _ in range(n):
        arr[int(input())] += 1
    for i in range(10001):
        if arr[i]:
            print(f'{i}\n' * arr[i], end='')

# sort_num_3()


import sys
input = sys.stdin.readline
arr = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    arr.append((x, y))

arr.sort(key=lambda a: (a[0], a[1]))
for x, y in arr:
    print(x, y)
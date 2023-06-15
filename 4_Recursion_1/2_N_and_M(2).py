
n, m = map(int, input().split())
arr = []
def recur(idx, pre):
    if idx == m:
        print(*arr)
        return
    for i in range(1, n+1):
        if i in arr:
            continue
        if pre > i:
            continue
        arr.append(i)
        recur(idx+1, i)
        arr.pop()

recur(0, -1)
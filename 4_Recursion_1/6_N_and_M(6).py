n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
res = []
idx = 0
pre = -1
def recur(idx, pre):
    if idx == m:
        print(*res)
        return
    for i in arr:
        if i in res:
            continue
        if i < pre:
            continue
        res.append(i)
        recur(idx+1, i)
        res.pop()

recur(idx, pre)
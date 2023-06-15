n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
res = []
idx = 0

def recur(idx):
    if idx == m:
        print(*res)
        return
    for i in arr:
        res.append(i)
        recur(idx+1)
        res.pop()

recur(idx)
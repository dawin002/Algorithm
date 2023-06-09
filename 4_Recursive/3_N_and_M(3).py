
n, m = map(int, input().split())
arr = []
def recur(idx):
    if idx == m:
        print(*arr)
        return
    for i in range(1, n+1):
        arr.append(i)
        recur(idx+1)
        arr.pop()

recur(0)
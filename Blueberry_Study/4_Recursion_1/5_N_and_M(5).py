
n, m = map(int, input().split())
arr = list(map(int, input().split()))
stack = []
arr.sort()

def recur(idx):
    if idx == m:
        print(*stack)
        return
    for i in arr:
        if i in stack:
            continue
        stack.append(i)
        recur(idx+1)
        stack.pop()

recur(0)
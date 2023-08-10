N = int(input())
arr = sorted(list(map(int, input().split())))
res = []
key = max(arr)

# key == ? + ? + ?
rec1 = [0 for _ in range(6)] + [key]
def recur1(idx):
    if idx == 6:
        return
    for x in range(rec1[idx], key):
        recur1(idx+1)
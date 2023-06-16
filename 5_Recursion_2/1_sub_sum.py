
n = int(input())
arr = list(map(int, input().split()))
res = set()

def recur(idx, sumi):
    if idx == n:
        res.add(sumi)
        return
    recur(idx+1, sumi + arr[idx])
    recur(idx+1, sumi)

recur(0, 0)

for i in range(9999999999999999):
    if i not in res:
        print(i)
        break
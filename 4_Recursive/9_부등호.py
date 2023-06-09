
k = int(input())
arr = list(input().split())
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
res = []

maxi = '0'
mini = '999999999999999'

idx = 0

def recur(idx, pre):
    if idx == k:
        global maxi
        global mini
        now_num = ''.join(map(str, res))
        if int(maxi) < int(now_num):
            maxi = now_num
        if int(mini) > int(now_num):
            mini = now_num
        return

    for i in nums:
        if i in res:
            continue
        if arr[idx] == '<':
            if not pre < i:
                continue
        elif arr[idx] == '>':
            if not pre > i:
                continue
        res.append(i)
        recur(idx+1, i)
        res.pop()

for i in nums:
    res.append(i)
    recur(0, i)
    res.pop()

print(maxi)
print(mini)
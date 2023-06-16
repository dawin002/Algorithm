n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

min_val = 99999999999999999999999999999
def recur(idx, choose_num, sin, ssun):
    if idx == n:
        global min_val
        if choose_num >= 1:
            min_val = min(min_val, abs(sin - ssun))
        return
    recur(idx+1, choose_num+1, sin * arr[idx][0], ssun + arr[idx][1])
    recur(idx+1, choose_num, sin, ssun)

recur(0, 0, 1, 0)
print(min_val)
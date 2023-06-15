n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
maxi = 0

def recur(date, money):
    if date > n:
        return
    if date == n:
        global maxi
        maxi = max(maxi, money)
        return

    recur(date + arr[date][0], money + arr[date][1])
    recur(date + 1, money)

recur(0, 0)

print(maxi)
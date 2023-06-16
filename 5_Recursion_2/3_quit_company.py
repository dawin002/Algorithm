
def recur(date, money):
    global maxi

    if date == n:
        maxi = max(maxi, money)
        return

    if date > n:
        return

    recur(date + arr[date][0], money + arr[date][1])
    recur(date + 1, money)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
maxi = 0

recur(0, 0)

print(maxi)
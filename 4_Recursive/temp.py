
n = int(input())
arr = [set(map(int, input().split())) for _ in range(n)]
maxi = 0
def recur(idx):
    if idx == n:
        if maxi < number:
            maxi = number

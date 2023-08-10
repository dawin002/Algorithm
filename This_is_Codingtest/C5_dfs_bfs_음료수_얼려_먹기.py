""" my code """


def dfs(x, y):
    if 0 <= x < N and 0 <= y < M:
        if icebox[x][y] == 0:
            icebox[x][y] = 1
            dfs(x, y + 1)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x - 1, y)
            return True
    return False


N, M = map(int, input().split())
icebox = [list(map(int, input())) for _ in range(N)]

count = 0

for i in range(N):
    for j in range(M):
        if dfs(i, j):
            count += 1

print(count)

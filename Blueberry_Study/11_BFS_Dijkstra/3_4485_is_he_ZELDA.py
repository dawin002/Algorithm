import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

test_case = 0
while True:
    test_case += 1
    n = int(input())
    if n == 0:
        break

    mmap = [list(map(int, input().split())) for _ in range(n)]
    distance = [[INF for _ in range(n)] for _ in range(n)]

    q = []
    heapq.heappush(q, (mmap[0][0], 0, 0))
    distance[0][0] = mmap[0][0]

    while q:
        cost, x, y = heapq.heappop(q)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if not(0 <= nx < n and 0 <= ny < n):
                continue
            nxt_cost = cost + mmap[nx][ny]
            if distance[nx][ny] > nxt_cost:
                distance[nx][ny] = nxt_cost
                heapq.heappush(q, (nxt_cost, nx, ny))

    print(f"Problem {test_case}: {distance[-1][-1]}")

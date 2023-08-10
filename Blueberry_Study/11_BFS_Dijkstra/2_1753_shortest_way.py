import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

V, E = map(int, input().split())
start = int(input())

graph = [[] for _ in range(V + 1)]
distance = [INF for _ in range(V + 1)]

for i in range(E):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

q = []
q.append((0, start))
distance[start] = 0

while q:
    dist, now = heapq.heappop(q)
    for node, cost in graph[now]:
        if distance[node] > dist + cost:
            distance[node] = dist + cost
            heapq.heappush(q, (dist + cost, node))

for c in distance[1::]:
    if c == INF:
        print('INF')
    else:
        print(c)
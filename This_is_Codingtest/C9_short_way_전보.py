""" 최단 경로 : 3. 전보 """


def dialCity():
    import heapq
    INF = int(1e9)
    n, m, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)

    for _ in range(m):
        x, y, z = map(int, input().split())
        graph[x].append((y, z))

    start = c

    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        d, now = heapq.heappop(q)
        if distance[now] < d:
            continue

        for vert in graph[now]:
            cost = d + vert[1]
            if distance[vert[0]] > cost:
                distance[vert[0]] = cost
                heapq.heappush(q, (cost, vert[0]))

    count = 0
    maxDis = 0
    for i in range(1, n + 1):
        if distance[i] < INF:
            count += 1
            maxDis = max(maxDis, distance[i])

    count -= 1  # 시작 노드 제외시키기!

    print('ans :', count, maxDis)

    print(distance)


# dialCity()


def new_sol():
    import heapq
    INF = int(1e9)
    n, m, start = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)

    for _ in range(m):
        a, b, dist = map(int, input().split())
        graph[a].append((dist, b))

    distance[start] = 0
    q = []
    count = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for cost, nv in graph[now]:
            cost += dist
            if distance[nv] > cost:
                distance[nv] = cost
                heapq.heappush(q, (cost, nv))

    res = 0
    for d in distance[1:]:
        if d != INF:
            count += 1
            res = max(res, d)
    count -= 1

    print(count, res)

new_sol()
""" 최단 경로 알고리즘 : 2. 미래 도시 """

# 1~N 번 회사
# 현재 1번에 있고 X번 회사에 가려고함
# 연결된 회사 양방향 이동 가능
# 회사간 거리 1
# X번 회사 가기 전 K번 회사도 가야됨
# 최소 시간 구하기
# 회사 수 N, 경유지 K, 목적지 X, 간선 튜플로 주어짐


# input
# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5
# ans
# 3



""" my code : 민힙 다익스트라 사용 ( 다익스트라 코드 참조 ) """
def futureCity() :
    import heapq
    INF = int(1e9)
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    x, k = map(int, input().split())
    # k = 목적지1, x = 목적지2

    graph = [[] for _ in range(n+1)]
    for a in arr :
        graph[a[0]].append((a[1], 1))
        graph[a[1]].append((a[0], 1))

    distanceK = [INF] * (n+1)
    # distanceK[0] = 0

    distanceX = [INF] * (n + 1)
    # distanceX[0] = 0

    def dijkstra(start, distance) :
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0

        while q :
            # now 까지 가는데 d 만큼 든대
            d, now = heapq.heappop(q)

            # 기록된(시작->now)거리 < 그래프(시작->now)거리 라면 건너 뛰어
            if distance[now] < d :
                continue

            # graph 의 now 행 (now->어딘가로 가는 간선들 기록)
            for i in graph[now]:
                # cost : (시작->now)거리 + (now->i[0])거리
                cost = d + i[1]
                # (시작->i[0])거리 > (시작->now->i[0]) 라면
                if distance[i[0]] > cost :
                    # (시작->i[0])거리 갱신
                    distance[i[0]] = cost
                    # 힙큐에 (갱신된 거리, i[0]) 넣기
                    heapq.heappush(q, (cost, i[0]))

    dijkstra(1, distanceK)
    dijkstra(k, distanceX)

    disK = distanceK[k]
    disX = distanceX[x]

    print(distanceK)
    print(distanceX)
    print(disK+disX)

# futureCity()


""" my code : 민힙 다익스트라 알고리즘 사용 ( 코드 비참조 ) """

def fCity() :
    import heapq
    INF = int(1e9)
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    x, k = map(int, input().split())
    graph = [ [] for _ in range(n+1)]
    for a in arr :
        graph[a[0]].append((a[1], 1))
        graph[a[1]].append((a[0], 1))
    distK = [INF] * (n + 1)
    distX = [INF] * (n + 1)

    def dijkstra(start, distance):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0 # 이 문장 까먹음!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        while q :
            d, now = heapq.heappop(q)
            if distance[now] < d :
                continue
            for vert in graph[now] :
                cost = d + vert[1]
                if distance[vert[0]] > cost :
                    distance[vert[0]] = cost
                    heapq.heappush(q, (cost, vert[0]))

    dijkstra(1, distK)
    dijkstra(k, distX)

    dK = distK[k]
    dX = distX[x]

    print(distK)
    print(distX)

    if dK + dX > INF :
        print(-1)
    else :
        print(dK + dX)

# fCity()


""" 정답 : 워셜 플로이드 알고리즘 이용 """

def fCity_ans() :
    INF = int(1e9)
    n, m = map(int, input().split())
    graph = [[INF] * (n+1) for _ in range(n + 1)]

    for ab in range(1, n+1) :
        graph[ab][ab] = 0

    for _ in range(m) :
        a, b = map(int, input().split())
        graph[a][b] = 1
        graph[b][a] = 1

    x, k = map(int, input().split())

    for k in range(1, n+1) :
        for a in range(1, n+1):
            for b in range(1, n+1):
                if graph[a][b] > graph[a][k] + graph[k][b]:
                    graph[a][b] = graph[a][k] + graph[k][b]

    distance = graph[1][k] + graph[k][x]

    for g in range(1, n+1):
        print(graph[g][1:])

    if distance > INF :
        print(-1)
    else :
        print(distance)

fCity_ans()
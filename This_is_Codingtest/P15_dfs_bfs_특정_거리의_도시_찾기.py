""" DFS/BFS 문제 : 15. 특정 거리의 도시 찾기 """

# 1~N번 도시 (2 <= N <= 300,000)
# M개의 단방향 도로 (1 <= M <= 1,000,000)
# 모든 도로 거리 1
# 특정 도시 X 출발, 최단 거리 K인 모든 도시 번호 출력
# (1 <= X <= N , 1 <= K <= 300,000)

def new_sol():
    from collections import deque
    INF = int(1e9)
    n, m, k, x = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)

    res = []
    distance = [INF] * (n+1)
    distance[x] = 0
    q = deque()
    q.append((0, x))

    while q:
        dist, now = q.popleft()
        for v in graph[now]:
            cost = dist + 1
            if distance[v] > cost:
                distance[v] = cost
                q.append((cost, v))

    for i in range(1, n+1):
        if distance[i] == k:
            res.append(i)

    if res:
        print('\n'.join(map(str, res)))
    else:
        print(-1)



new_sol()


""" my solution """

def find_k_dist_city():
    # 필요 항목 초기화 부분
    from collections import deque

    INF = int(1e9)
    n, m, k, x = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)

    start_x = [INF] * (n+1)
    start_x[x] = 0

    # 알고리즘 부분 (BFS)
    q = deque([x])  # 큐에 요소로 x 넣고 시작
    while q:
        now = q.popleft()
        for next in graph[now]:
            if start_x[next] > start_x[now] + 1:
                start_x[next] = start_x[now] + 1
                q.append(next)

    # 정답 출력 부분
    answer = []
    for end in range(1, len(start_x)):
        if start_x[end] == k:
            answer.append(end)
    if answer:
        print('\n'.join(map(str, answer)))
    else:
        print(-1)

find_k_dist_city()

# input1
# 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4

# input2
# 4 3 2 1
# 1 2
# 1 3
# 1 4

# input3
# 4 4 1 1
# 1 2
# 1 3
# 2 3
# 2 4
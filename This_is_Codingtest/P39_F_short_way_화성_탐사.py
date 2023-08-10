""" 최단 경로 문제 : 39. 화성 탐사 """

# n * n 지도
# 각 칸 지나기 위한 비용 다름
# (0, 0) 출발 (끝, 끝) 도착
# 상하좌우 인접칸 이동 가능
# 도착 필요 비용 최소값 출력

""" answer solution """

# 배워야 할 것
# 데이터 크면 다익스트라 활용하자!
# 다익스트라로 풀면 g[x][y] 에서 4방향으로 가는 edge들 3차원 리스트로 처리할 필요 없음
# 단, INF 로 채우는 distance 리스트는 2차원으로 만들어야함
# 우선순위 큐에 넣는 원소 : (비용, x좌표, y좌표)

def mars_adventure():
    import heapq
    INF = int(1e9)
    # 4 방향 지정
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    n = int(input())
    # 그냥 지도 받아오면 됨
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))

    # 각 노드까지 가는 최소 비용 (2차원 리스트 선언)
    distance = [[INF] * n for _ in range(n)]

    x, y = 0, 0

    q = []
    heapq.heappush(q, (graph[x][y], x, y))
    # 출발지점 비용 갱신
    distance[x][y] = graph[x][y]

    # 다익스트라 알고리즘 실행
    while q:
        dist, x, y = heapq.heappop(q)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + graph[nx][ny]
                if distance[nx][ny] > cost:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

    # 다익스트라 결과 출력
    for line in distance:
        print(line)

    return distance[n - 1][n - 1]


def solution():
    for i in range(int(input())):
        result = mars_adventure()
        print(result)


solution()

# 입력
# 3
# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5
# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4

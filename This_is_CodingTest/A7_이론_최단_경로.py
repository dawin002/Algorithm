""" 최단 경로 : Shortest Path """

# 카테고리
#     다익스트라 최단 경로 알고리즘
#         - 간단한 다익스트라 알고리즘
#         - 개선된 다익스트라 알고리즘
#     플로이드 워셜 알고리즘

# 가장 짧은 경로를 찾는 알고리즘
# 한 지점에서 한 지점까지의 최단 경로 (다익스트라)
# 모든 지점에서 다른 모든 지점까지의 최단 경로 (플로이드 워셜)
# 보통 그래프를 이용해 표현
# 그리디 , 다이나믹 프로그래밍 두 알고리즘이 최단 경로 알고리즘에 적용


""" 다익스트라 최단 경로 알고리즘 """

# 특정 노드에서 출발해서 다른 노드로 가는 각각의 최단경로 구하는 알고리즘
# 그리디에 포함됨 : 매번 가장 비용이 적은 노드 선택

# 원리
# 1. 출발 노드 설정
# 2. 최단 거리 테이블 초기화
# 3. 방문하지 않은 노드 중 최단거리 가장 짧은 노드 선택
# 4. 해당 노드 거쳐 다른 노드 가는 비용 계산 후 테이블 갱신
# 5. (3,4) 과정 반복

# 두 가지 구현 방법 : 쉽지만 느린 코드 / 어렵지만 빠른 코드

# 다익스트라 - 간단한 알고리즘

def dijkstra_simple():
    INF = int(1e9)
    n, m = map(int, input().split())  # 노드, 간선 개수 입력
    graph = [[] for _ in range(n + 1)]  # 각 노드에 연결된 노드 정보 담는 리스트
    start = int(input())  # 시작 노드 번호 입력
    for _ in range(m):  # 노드 정보 입력 ( 출발, 도착, 비용 )
        s, e, d = map(int, input().split())  # s에서 e가는데 d비용 든다
        graph[s].append((e, d))

    visited = [False] * (n + 1)
    distance = [INF] * (n + 1)

    # 방문 안한 노드 중에서 가장 짧은 노드 번호 반환
    def get_smallest_node():
        min_value = INF
        index = 0  # 가장 짧은 노드 인덱스
        for i in range(1, n + 1):
            if distance[i] < min_value and not visited[i]:
                min_value = distance[i]
                index = i
        print('smallest node :', index)  ###############################
        return index

    # 다익스트라 알고리즘
    def dijkstra(start):
        # 시작 노드에 대해서 초기화
        distance[start] = 0  # 시작노드 스스로 가는 비용 0
        visited[start] = True  # 시작노드 방문 표시
        for vertex in graph[start]:  # 시작노드와 인접한 노드 탐색
            nv, cost = vertex
            distance[nv] = cost  # 시작노드와 인접한 노드 비용 초기화

        # 시작 노드를 제외한 전체 n-1 개의 노드에 대해 반복
        for _ in range(n - 1):
            # 현재 최단거리가 가장 짧은 노드를 꺼내서 방문 처리
            now = get_smallest_node()
            visited[now] = True
            # 현재 노드와 연결된 다른 노드를 확인
            for vertex in graph[now]:
                cost, nv = vertex
                # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                if distance[nv] > distance[now] + cost:
                    distance[nv] = distance[now] + cost
                print('distance :', distance)
            print('visited :', visited)

    # 다익스트라 알고리즘 실행
    dijkstra(start)

    # 모든 노드로 가기 위한 최단 거리를 출력
    for i in range(1, n + 1):
        # 도달할 수 없으면 INF 출력
        if distance[i] == INF:
            print('INFINITY')
        else:
            print(distance[i])


# dijkstra_simple()

###
# input
# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2


""" 개선된 다익스트라 알고리즘 (우선순위큐 이용)  """

# 심플 다익스트라는 O(N^2)이라 너무 느림
# 최소비용 방문안한 노드 선형탐색으로 찾는게 오래걸림 (get_shortest_node() 함수)
# 힙큐로 우선순위큐 만들어 가장 최소비용 노드 뽑음
# 시간복잡도 O(ElogV) (E 간선수, V 노드수)

# 힙큐에 데이터 묶음(리스트,튜플 등) 넣으면 첫번째 원소 기준으로 우선순위 정렬됨
# heapq.heappop(큐)로 꺼내면 가장 작은 값이 pop됨
# 큐에 데이터가 있는동안 비용 가장 작은 노드 꺼내고, 방문한 노드인지 확인, 최소비용 갱신 순으로 동작

def dijkstra_advanced():
    import heapq
    INF = int(1e9)
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    start = int(input())

    for _ in range(m):
        s, e, d = map(int, input().split())
        graph[s].append((d, e))

    distance = [INF] * (n + 1)

    def dijkstra():
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0

        while q:
            dist, now = heapq.heappop(q)

            if distance[now] < dist:
                continue

            for cost, next_v in graph[now]:
                cost = dist + cost
                if cost < distance[next_v]:
                    distance[next_v] = cost
                    heapq.heappush(q, (cost, next_v))

    dijkstra()

    for i in range(1, n + 1):
        if i == INF:
            print(-1)
        else:
            print(distance[i])

# dijkstra_advanced()


""" 플로이드 워셜 알고리즘 """

# Floyd-Warshall Algorithm

# 모든 노드에서 다른 모든 노드까지의 최단 경로 모두 구하기
# 노드수 N일때 N 단계에서 각 단계에 N^2회의 연산을 수행
# 시간복잡도 O(N^3)

# 2차원 리스트에 '최단거리' 정보 저장
# 다이나믹 프로그래밍의 특징 : N단계를 반복하며 점화식에 맞게 2차원 리스트 갱신
# A 노드를 고려하는 단계에서 A를 거쳐갈 수 있는 모든 경로(출발->도착)에 대해
# 비용(출발->도착) = min( 비용(출발->도착), 비용(출발->A->도착) ) 의 값으로 갱신한다


def floyd_warshall():
    INF = int(1e9)

    n = int(input())
    m = int(input())
    graph = [[INF] * (n+1) for _ in range(n + 1)]

    # 자기자신 -> 자기자신 비용 0으로 초기화
    for ab in range(1, n+1):
        graph[ab][ab] = 0

    # 각 간선 정보 입력받고 테이블 초기화
    for _ in range(m):
        # a 에서 b 로 가는 비용 c
        a, b, c = map(int, input().split())
        graph[a][b] = c

    # 점화식에 따라 플로이드 워셜 알고리즘 수행
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

    # 수행된 결과 출력
    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][b] == INF:
                print(-1, end=' ')
            else:
                print(graph[a][b], end=' ')
        print()

floyd_warshall()

# input
# 4
# 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2
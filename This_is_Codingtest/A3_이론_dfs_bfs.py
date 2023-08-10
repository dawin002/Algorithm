""" 깊이 우선 탐색 / 너비 우선 탐색 : DFS / BFS """

# 카테고리
#     스택 Stack
#     큐 Queue
#     재귀함수
#     그래프
#     깊이 우선 탐색 DFS
#     너비 우선 탐색 BFS

# 탐색 : 많은 양의 데이터 중 원하는 데이터를 찾는 것


""" 스택 : Stack """

# 선입후출, FILO, First In Last Out

def my_stack():
    stack = []
    stack.append('1')
    stack.append('2')
    stack.append('3')
    while stack:
        a = stack.pop()
        print(a, end=' ')  # => 3 2 1


""" 큐 : Queue """

# 선입선출, FIFO, First In First Out

# q = deque() 객체를 List 로 바꾸려면 : list(q)

def my_queue():
    from collections import deque
    q = deque()
    q.append('1')
    q.append('2')
    q.append('3')
    while q:
        a = q.popleft()
        print(a, end=' ')  # => 1 2 3

    q = list(q)  # => q = []


""" 재귀 함수 : Recursive Function """

# 자기 자신을 다시 호출하는 함수
# 종료 조건 반드시 명시해야 함

# 대표적으로 팩토리얼
#     n == 0 or 1 : n! = 1
#     n > 1       : n! = n * (n-1)!
def factorial(n):
    if n <= 1:
        return n
    return n * factorial(n-1)


""" 그래프 : Graph """

# 노드와 간선에 대한 정보를 가진 자료구조

# 노드 : Node
#     값을 저장할 수 있는 지점

# 간선 : Edge
#     노드와 노드를 연결하는 선
#     방향과 가중치 있을 수 있음

# 표현 방식
#     인접 행렬
#     인접 리스트

# 인접 행렬 방식
#     2차원 배열로 그래프의 연결 관게를 표현하는 방식
#     2차원 배열에 각 노드가 연결된 형태를 기록

def graph_adjacency_matrix():
    INF = int(1e9)
    n = 3
    nodes = [1, 2, 3]
    edges = [(1, 2, 6), (2, 1, 7), (3, 2, 5)]  # (x, y, cost)
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n+1):
        graph[i][i] = i

    for edge in edges:
        x, y, cost = edge
        graph[x][y] = cost
        # graph[y][x] = cost  # 무방향 그래프라면 역화살표도 추가

    for line in graph[1:]:
        print(' '.join(map(str, line)))


# 인접 리스트 방식
#     리스트로 그래프의 연결 관계를 표현하는 방식
#     모든 노드에 연결된 노드에 대한 정보를 연결하여 저장

def graph_():
    INF = int(1e9)
    n = 3
    nodes = [1, 2, 3]
    edges = [(1, 2, 6), (2, 1, 7), (3, 2, 5)]  # (x, y, cost)
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for edge in edges:
        x, y, cost = edge
        graph[x].append((y, cost))

    for line in graph[1:]:
        print(' '.join(map(str, line)))

"""
    인접 행렬 방식 vs 인접 리스트 방식
    
    인접 행렬 방식  : 특정 두 노드의 연결 상태에 바로 접근하거나 상태를 바꿔야할 때 사용하면 편함
                   특정 두 노드 연결되어 있는지 바로 확인 가능
                   but, 메모리 공간 많이 사용
                   
    인접 리스트 방식 : 특정 노드와 연결된 모든 인접 노드를 순회해야 하는 경우 사용
                   메모리 공간 낭비 적음
                   but, 특정 두 노드 연결되어 있는지 탐색 속도 느림
"""


""" 깊이 우선 탐색 : DFS (Dephth-First-Search) """

# 그래프에서 깊은 노드를 우선적으로 탐색하는 알고리즘
# 특정한 경로로 탐색하다가 특정한 상황에서 최대한 깊숙이 들어가서 노드를 방문하고, 다시 돌아나가 다른 경로를 탐색
# 스택 자료구조 이용(원리는 스택, 구현은 재귀함수)
# 시간복잡도 O(N)

# 구체적인 동작 과정
#     1. 탐색 시작 노드를 스택에 삽입하고 방문 처리, 결과에 추가
#     2. 스택의 최상단 노드의 인접 노드 중
#         1) 방문하지 않은 노드가 있으면 : 그 인접노드 스택에 넣고 방문 처리, 결과에 추가
#         2) 방문하지 않은 노드가 없으면 : 스택에서 최상단 노드 꺼냄
#     3. 스택에서 모든 노드가 꺼내질 때까지 2번 과정 반복

def my_dfs():
    n = 8
    graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
    visited = [False] * (n + 1)
    result = []

    def dfs(graph, v, visited):
        visited[v] = True
        result.append(v)
        print(v, end=' ')
        for next_v in graph[v]:
            if not visited[next_v]:
                dfs(graph, next_v, visited)

    dfs(graph, 1, visited)
    print('\n', result, sep='')
    return result

my_dfs()


""" 너비 우선 탐색 : BFS (Breadth First Search) """

# 그래프에서 가까운 노드를 우선적으로 탐색하는 알고리즘
# 인접한 노드를 반복적으로 큐에 넣고 큐에서 나오는 순으로 노드를 방문하는 방식
# 큐 자료구조 이용(원리도 큐, 구현도 큐)
# 시간복잡도

# 구체적인 동작 과정
#     1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
#     2. 큐에서 노드를 꺼내고 결과에 추가
#     3. 꺼낸 노드의 인접 노드 중 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
#     4. 큐에서 모든 노드를 꺼낼 때까지 2,3번 과정 반복

def my_bfs():
    from collections import deque

    n = 8
    graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
    visited = [False] * (n + 1)
    result = []
    start = 1

    def bfs(graph, start, visited):
        queue = deque([start])
        visited[start] = True
        while queue:
            v = queue.popleft()
            print(v, end=' ')
            result.append(v)
            for next_v in graph[v]:
                if not visited[next_v]:
                    queue.append(next_v)
                    visited[next_v] = True

    bfs(graph, start, visited)
    print('\n', result, sep='')
    return result

    # 잘못된 bfs 함수
    # def bfs_wrong(graph, start, visited):
    #     queue = deque([start])
    #     while queue:
    #         v = queue.popleft()
    #         visited[v] = True  ####### visited[v] = True 를 여기에 넣으면 안되는 이유
    #         print(v)
    #         result.append(v)
    #         for next_v in graph[v]:
    #             if not visited[next_v]:
    #                 queue.append(next_v)
    #                 ########## 큐에 노드 넣을때 visited 처리 안해서 동일 노드 여러번 추가됨

my_bfs()

""" 
    dfs, bfs 구현시 방문 처리 시점
    dfs : 재귀함수 시작하면서 현재 노드 방문 처리
    bfs : 초기상태에서 시작 노드 방문처리, 꺼낸 노드의 인접 노드들 큐에 넣으면서 방문 처리 
"""

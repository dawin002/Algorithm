""" 그래프 이론 : Graph Theory"""

# 카테고리
#     서로소 집합
#         - 서로소 집합 알고리즘
#         - 서로소 집합 알고리즘 - 사이클 판별
#     신장 트리
#         - 최소 신장 트리
#         - 크루스칼 알고리즘
#     위상 정렬 알고리즘

""" 서로소 집합 : Disjoint Sets """

# 공통 원소가 없는 두 집합
# 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
# union 연산 (합집합)
#     : 원소가 포함된 2개의 집합을 하나의 집합으로 합치는 연산
# find 연산 (찾기)
#     : 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산
# 두 집합이 서로소 관계인지 확인할 수 있다

""" 서로소 집합 알고리즘 """

# 트리 자료구조 이용해 서로소 집합을 계산하는 알고리즘
# union 연산을 효과적으로 수행하기 위해 parent 테이블을 항상 가지고 있어야 함
# 루트 노드를 즉시 계산할 수 없고, find 연산으로 parent 테이블을 거슬러 올라가야 함
# (더 이상 부모 노드가 없을 때의 현재 노드가 루트 노드)

# 동작 과정
# 1. union(합집합) 연산을 확인하여 서로 연결된 두 노드 A, B 확인
#     1) A와 B의 루트노드 A', B'을 각각 찾는다
#     2) A'을 B'의 부모 노드로 설정(B'이 A'을 가리키게)
# 2. 모든 union 연산을 처리할 때까지 1 과정을 반복


""" 서로소 집합 알고리즘 - 경로 압축 기법 """

# 루트를 확인하기 위해 find 연산으로 parent 테이블을 거슬러 올라가는 것을 최적화한 기법
# 재귀함수인 find 연산을 수정해 parent 테이블에 해당 노드의 부모 노드를 저장하는 게 아닌
# 해당 노드가 속한 집합의 루트 노드를 저장하도록 하는 기법
# 사실상 parent 테이블이 아니라 root 테이블이 된 것
# 시간 복잡도 : O(V+M(1+log_(2-M/V)V) (V:노드 수, M:find 횟수, V-1:union 횟수)


def disjoint_sets():
    # 특정 원소가 속한 집합의 루트 찾기 ( 압축 기법 미적용 - 비효율적 )
    def find_parent_original(parent, x):
        # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
        if parent[x] != x:
            return find_parent_original(parent, parent[x])
        return x

    # 압축 기법 적용된 루트 찾기 (부모를 루트로 갱신시킴, 바로 위 함수랑 차이 구분할 것 )
    def find_parent(parent, x):
        if parent[x] != x:  # x가 루트가 아니라면
            parent[x] = find_parent(parent, parent[x])  # x의 루트 = 루트찾기(부모 리스트, x의 부모)
        return parent[x]  # x의 부모(루트) 반환

    # 두 원소가 속한 집합을 합치기
    def union_parent(parent, a, b):
        a = find_parent(parent, a)  # a의 루트 찾기
        b = find_parent(parent, b)  # b의 루트 찾기
        # 더 작은 루트 노드를 큰 루트 노드의 루트로 지정
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    # 노드의 개수와 간선(union 연산)의 개수 입력받기
    v, e = map(int, input().split())
    parent = [0] * (v + 1)  # 부모 테이블 초기화

    # 부모 테이블상에서, 부모를 자기 자신으로 초기화
    for i in range(1, v + 1):
        parent[i] = i

    # union 연산을 각각 수행
    for i in range(e):
        a, b = map(int, input().split())
        union_parent(parent, a, b)

    # 각 원소가 속한 집합 출력
    print('각 원소가 속한 집합: ', end=' ')
    for i in range(1, v + 1):
        print(find_parent(parent, i), end=' ')

    print()

    # 부모 테이블 내용 출력
    print('부모 테이블: ', end=' ')
    for i in range(1, v + 1):
        print(parent[i], end=' ')
# Disjoint_sets()

# input
# 6 4
# 1 4
# 2 3
# 2 4
# 5 6


""" 서로소 집합 알고리즘 - 무방향 그래프 사이클 판별 """

# 서로소 집합 알고리즘 이용해 무방향 그래프 내에서의 사이클을 판별할 수 있음
# *방향 그래프의 사이클 여부는 DFS이용해 판별 가능
# 간선(union 연산)을 하나씩 확인하면서 두 노드가 포함되어 있는 집합을 합쳤치는 과정에서
# 두 노드의 루트가 union 하기 전에 이미 같다면 사이클이 있다는 뜻

# 동작 과정
# 1. 각 간선을 확인하며 두 노드의 루트 노드를 확인
#     1) 루트 노드가 서로 다르면 두 노드 union
#     2) 루트 노드가 같다면 사이클이 발생한 것
# 2. 그래프에 포함되어 있는 모든 간선에 대해 1번 과정 반복

def check_cycle():
    # 특정 원소가 속한 집합 찾기
    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    # 두 원소가 속한 집합을 합치기
    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    # 노드의 개수와 간선(union 연산)의 개수 입력받기
    v, e = map(int, input().split())

    # 부모 테이블 초기화 및 부모값 자기 자신으로 초기화
    parent = [i for i in range(v + 1)]

    cycle = False  # 사이클 발생 여부

    for _ in range(e):
        a, b = map(int, input().split())
        # 사이클 발생한 경우 종료
        if find_parent(parent, a) == find_parent(parent, b):
            cycle = True
            break
        # 사이클 발생하지 않았다면 합집합(union) 수행
        else:
            union_parent(parent, a, b)

    if cycle:
        print("사이클 발생")
    else:
        print("사이클 발생하지 않음")


# check_cycle()

# input
# 3 3
# 1 2
# 1 3
# 2 3


""" 신장 트리 - 크루스칼 알고리즘 : Kruskal Algorithm"""

# 신장 트리
#     하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
#     모든 노드 포함 + 사이클 없음 == 트리의 성립 조건

# 최소 신장 트리
#     신장 트리 중에서 간선 비용의 합이 최소가 되는 신장 트리
#     일동의 트리 자료구조로 최종적으로 신장 트리에 포함되는 간선의 개수 '노드 개수 -1'개

# 최소 신장 트리 알고리즘
#     신장 트리 중에서 최소 비용으로 만들 수 있는 신장 트리를 찾는 알고리즘
#     그 중에 하나가 '크루스칼 알고리즘'

# 크루스칼 알고리즘 : Kruskal Algorithm
#     그리디 알고리즘 이용
#     간선의 비용에 대해 정렬 후 가장 짧은 비용의 간선부터 집합에 포함시는 알고리즘
#     단, 사이클을 발생시키지 않는 간선에 한해서 집합에 포함!
#     시간 복잡도 : O(ElogE) (E:간선 개수)

# 동작 과정
# 1. 간선 데이터를 비용에 따라 오름차순으로 정렬
# 2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
#     1) 사이클이 발생하지 않으면 최소 신장 트리에 포함시킴
#     2) 사이클이 발생하면 추가하지 않고 넘어감
# 3. 모든 간선에 대해 2번 과정 반복

def kruskal_algorithm():
    # 특정 원소가 속한 집합을 찾기
    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    # 두 원소 속한 집합 합치기
    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    # 노드의 개수와 간선(union 연산)의 개수 입력받기
    v, e = map(int, input().split())

    # 모든 간선을 담을 리스트와 최종 비용을 담을 변수
    edges = []
    result = 0

    # 부모 테이블에서 부모를 자기 자신으로 초기화
    parent = [0] * (v + 1)
    for i in range(1, v + 1):
        parent[i] = i

    # 모든 간선에 대한 정보를 입력받기
    for i in range(e):
        v1, v2, cost = map(int, input().split())
        edges.append((cost, v1, v2))

    # 간선을 비용순으로 정렬
    edges.sort()

    # 간선을 하나씩 확인
    for edge in edges:
        cost, v1, v2 = edge
        if find_parent(parent, v1) != find_parent(parent, v2):
            union_parent(parent, v1, v2)
            result += cost

    print(result)


# kruskal_algorithm()

# input
# 7 9
# 1 2 29
# 1 5 75
# 2 3 35
# 2 6 34
# 3 4 7
# 4 6 23
# 4 7 13
# 5 6 53
# 6 7 25
# ans
# 159


""" 위상 정렬 알고리즘 """

# 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것
# 정렬 알고리즘의 일종
# 순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할 때 사용
# 그래프상에서 노드간의 선후 관계가 있다면 모든 선후 관계를 지키는 전체 순서 구할 수 있음
# 큐 자료구조나 스택 자료구조 이용해 구현

# 진입차수 Indegree 테이블 사용
# *진입차수 : 특정 노드로 들어오는 간선의 개수

# 시간 복잡도 : O(V+E)  (V:노드 수, E:간선 수)

# 동작 과정
# 1. 각 노드의 진입차수 계산
# 2. 진입 차수가 0인 노드를 큐에 넣음
# 3. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거
#    (그 노드에서 출발해 도착하는 노드의 진입 차수 1씩 감소)
# 4. 새롭게 진입 차수가 0이 된 노드 큐에 넣음
# 5. 큐가 빌 때까지 3,4번 과정 반복
# 참고 : 결과로 나온 노드가 전체 노드 수와 같지 않다면 사이클 존재

def topology_sort():
    from collections import deque

    # 노드 개수, 간선 개수 입력받기
    v, e = map(int, input().split())
    # 모든 노드에 대한 진입차수 0으로 초기화
    indegree = [0] * (v + 1)
    # 각 노드에 연결된 간선 정보 담기 위한 연결 리스트(그래프) 초기화
    graph = [[] for _ in range(v + 1)]

    # 방향 그래프의 모든 간선 정보 입력받기
    for _ in range(e):
        a, b = map(int, input().split())
        # 노드 a에서 갈 수 있는 노드 리스트에 b 추가
        graph[a].append(b)
        # 진입차수 1 증가
        indegree[b] += 1

    ##### 위상 정렬 시작 #####

    result = []  # 알고리즘 수행 결과 담을 리스트
    q = deque()  # 큐 생성

    for i in range(1, v + 1):
        if indegree[i] == 0:
            # start = i     # 틀렸음 : 진입차수 0인 노드 전부 삽입해야함 (하나만 넣어서 틀림)
            q.append(i)
    # q.append(start)       # 틀렸음 : 동일 이유

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소에서 출발해 도착하는 노드들 진입차수 1 감소
        for arrive in graph[now]:
            indegree[arrive] -= 1
            # 새롭게 진입차수가 0이 된 노드 큐에 삽입
            if indegree[arrive] == 0:
                q.append(arrive)

    # 전체 노드 수보다 큐에서 나온 노드 수가 적으면 사이클 존재
    if v > len(result):
        print("Cycle exist : v != len(result)")
        print(f'v = {v} , len(res) = {len(result)}')
    # 결과 출력
    else:
        print()
        print('result =', *result)


# topology_sort()

# input
# 7 8
# 1 2
# 1 5
# 2 3
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4

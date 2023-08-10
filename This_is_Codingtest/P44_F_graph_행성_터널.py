""" 그래프 이론 문제 : 44. 행성 터널 """

# n 개 행성
# 모든 행성 연결하는 터널 만들 것
# 행성 위치 : 3차원 좌표
# 두 행성 A(x1, y1, z1), B(x2, y2, z2) 사이 거리 : min(|x1-x2|, |y1-y2|, |z1-z2|)
# 총 n-1개 터널 만들어 모든 행성 연결
# 최소 비용 출력

""" my solution : 틀렸음 """

"""
내 풀이 시간복잡도 ==> 최악의 경우 10만^2 계산 횟수
node 최대 10만 개여서 중복 제거 하고도 (10만 * 10만-1 / 2) 개의 edge 비교 해야함
==> 어떻게 하면 적은 수의 edge 만 비교할 수 있을 지 고민해야 하는 문제
핵심 아이디어 : 
          1. 어차피 x축은 x축끼리, y=y끼리, z=z끼리, 같은 좌표계끼리 비교한다
          2. x축 좌표로 정렬했을 때 x[5] <--> x[6] 거리보다 x[5] <--> x[7] 거리가 가까울 수 없다
             ==> 한 축으로 정렬했다면 바로 옆 노드끼리만 비교해서 거리 구하면 된다, 인접하지 않은 노드는
                 계산할 필요 없다
          단, a <--> b 노드가 여러 개의 최소 거리인 edge를 가지고 있어 
          (minX, a, b), (minY, a, b) 두 개 이상의 edge가 그래프에 들어갈 수 있으므로
          사이클이 형성되지 않는지 체크해야함
"""


# n개 행성에 총 n-1 개 터널? ==> 최소 비용 신장 트리

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def planet_tunnel():
    n = int(input())
    planets = []
    for _ in range(n):
        planets.append(tuple(map(int, input().split())))

    parent = [i for i in range(n)]

    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1, z1 = planets[i]
            x2, y2, z2 = planets[j]
            cost = min(abs(x1 - x2), abs(y1 - y2), abs(z1 - z2))
            edges.append((cost, i, j))

    edges.sort()

    result = 0

    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) == find_parent(parent, b):
            continue
        union_parent(parent, a, b)
        result += cost

    print(result)


planet_tunnel()


""" answer solution """


def planet_tunnel_ans():
    n = int(input())
    parent = [i for i in range(n + 1)]

    edges = []
    result = 0

    x = []
    y = []
    z = []

    # 모든 노드에 대한 좌표 값 입력받아 좌표계 분리해서 넣기
    for i in range(1, n + 1):
        data = list(map(int, input().split()))
        x.append((data[0], i))
        y.append((data[1], i))
        z.append((data[2], i))

    x.sort()
    y.sort()
    z.sort()

    # 인접한 노드들로부터 간선 정보를 추출하여 처리
    for i in range(n-1):
        # 비용 순으로 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정
        # 각 튜플 원소: (x축 기준 인접한 두 행성 거리, 그 행성1 번호, 그 행성2 번호)
        edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
        edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
        edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

    # 간선 비용 순으로 정렬
    edges.sort()

    # 간선을 하나씩 확인하며 최소 비용 신장 트리 생성
    for edge in edges:
        cost, a, b = edge
        # 루트가 같지 않다면 집합에 포함 (루트 같으면 사이클)
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost

    print(result)

planet_tunnel_ans()

# input1
# 5
# 11 -15 -15
# 14 -5 -15
# -1 -1 -5
# 10 -4 -1
# 19 -4 19

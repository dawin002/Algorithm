""" 그래프 이론 : 3. 도시 분할 계획 """

# 시작시간 : 1545
# 풀이시간 : 40분
# 마감시간 : 1625

# 집 n 개 도로 m 개
# 2개의 분리된 마을 계획
# 두 마을 건너가는 길들 없앰
# 각 마을 집들 사이 유지비 최소로
# 첫째줄 : 1 < n < 10만, 0 < m < 100만
# 2 ~ m+1 줄 : a, b, c : 집1, 집2, 유지비 (0 < c < 1천)
# 출력 : 나눠진 두 마을의 유지비 합의 최소값

def new_solution():

    def find_p(parent, x):
        if parent[x] != x:
            parent[x] = find_p(parent, parent[x])
        return parent[x]

    def union(parent, a, b):
        a = find_p(parent, a)
        b = find_p(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    n, m = map(int, input().split())
    edges = []

    parent = [i for i in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((c, a, b))

    edges.sort()
    # edges.sort(key=lambda x: (-x[0], x[1]))

    res = []
    result = 0

    for edge in edges:
        c, a, b = edge
        if find_p(parent, a) != find_p(parent, b):
            union(parent, a, b)
            result += c
            last = c
    #
    # while edges:
    #     c, a, b = edges.pop()
    #     if find_p(parent, a) != find_p(parent, b):
    #         union(parent, a, b)
    #         res.append(c)
    # print(sum(res) - max(res))

    print(result - last)

new_solution()


def splitCityPlan():
    import heapq
    n, m = map(int, input().split())
    parent = [i for i in range(n+1)]

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

    edges = []
    result = []
    for _ in range(m):
        a, b, cost = map(int, input().split())
        heapq.heappush(edges, (cost, a, b))
    # print('edges  :', edges)
    # print('parent :', parent)

    while edges:
        cost, a, b = heapq.heappop(edges)
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            heapq.heappush(result, -cost)
    # print('edges  :', edges)
    # print('parent :', parent)
    # print('result :', result)
    heapq.heappop(result)

    sum = 0
    for res in result:
        sum += -res

    print(sum)

splitCityPlan()

# input
# 7 12
# 1 2 3
# 1 3 2
# 3 2 1
# 2 5 2
# 3 4 4
# 7 3 6
# 5 1 5
# 1 6 2
# 6 4 1
# 6 5 3
# 4 5 3
# 6 7 4

""" answer code """

def splitCityPlan_ans():

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

    n, m = map(int, input().split())
    parent = [i for i in range(n+1)]

    edges = []
    result = 0      # 이 부분이 다름

    for _ in range(m):
        a, b, cost = map(int, input().split())
        edges.append((cost, a, b))

    edges.sort()
    last = 0

    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
            last = cost


    print(result-last)

splitCityPlan_ans()
""" 그래프 이론 문제 : 43. 어두운 길 """

# n 개 집
# m 개 도로
# 각 도로 가로등 비용 == 도로 거리
# 전체 도로 최소 신장 그래프의 전체 가로등 비용

""" my solution : 정답 """

"""
정답 코드에서는 그냥 sort() 로 정렬, 내 코드는 heapq 의 heappush(), heappop() 사용
알아본 결과 : 정렬된 채로 새로운 원소 넣기 / 가장 작은 값 꺼내기 연산이 필요한 경우가 아니면
           그냥 리스트를 입력 받고 한번에 sort() 한 후 작은 값부터 꺼내는 게 더 빠르다
결론 : 원소 추가 / 제거 될 때마다 sort() 해야 하는 문제면 heapq 이용할 것!
"""

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

def dark_road():
    n, m = map(int, input().split())
    parent = [i for i in range(n)]
    edges = []
    for _ in range(m):
        x, y, z = map(int, input().split())
        edges.append((z, x, y))

    edges.sort()

    result = 0
    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) == find_parent(parent, b):
            result += cost
            continue
        union_parent(parent, a, b)

    print(result)

dark_road()

# input1
# 7 11
# 0 1 7
# 0 3 5
# 1 2 8
# 1 3 9
# 1 4 7
# 2 4 5
# 3 4 15
# 3 5 6
# 4 5 8
# 4 6 9
# 5 6 11
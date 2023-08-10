""" 그래프 이론 문제 : 41. 여행 계획 """

# 1~n 번, 총 n 개 여행지
# 양방향 도로 있음
# 여행 계획 도시 수 m
# n 개 줄 입력 : n x n 지도 (그래프 연결 리스트)
# 지도 1 : 연결됨, 0 : 연결 안됨
# 마지막 줄 입력 : 여행 계획 도시들

""" my solution """

def travel_plan():

    def find_parent(parent, x):
        if parent[x] == x:
            return x
        parent[x] = find_parent(parent, parent[x])
        return parent[x]

    def union(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    n, m = map(int, input().split())

    parent = [i for i in range(n)]

    for i in range(n):
        line = list(map(int, input().split()))
        for j in range(n):
            if line[j] == 1:
                union(parent, i, j)

    plan = list(map(int, input().split()))
    for i in range(m):
        plan[i] -= 1

    root = parent[plan[0]]
    for city in plan:
        if parent[city] != root:
            print('NO')
            break
    else:
        print('YES')

    # 책 풀이 나랑 다른 부분 : 여행 계획 도시 모두 루트 같은지 확인하기 (나도 맞음)
    # result = True
    # for i in range(m-1):
    #     if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
    #         result = False
    # if result == True:
    #     print('YES')
    # else:
    #     print('NO')

    print(parent)

# travel_plan()


# 입력
# 5 4
# 0 1 0 1 1
# 1 0 1 1 0
# 0 1 0 0 0
# 1 1 0 0 0
# 1 0 0 0 0
# 2 3 4 3
# YES

# 입력2
# 5 4
# 0 1 0 1 0
# 1 0 1 1 0
# 0 1 0 0 0
# 1 1 0 0 0
# 0 0 0 0 0
# 2 3 5 4
# NO
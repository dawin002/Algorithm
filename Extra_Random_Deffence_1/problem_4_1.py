# 그래프
import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 각 노드의 루트 노드 저장하는 parent 리스트
parent = [i for i in range(n + 1)]  # 자기 자신을 루트로 가지는 초기 상태


# x 노드의 루트 노드 찾는 함수
def find_parent(x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]


# a, b 가 속한 트리를 합치는 함수
def union_parent(a, b):
    root_a = find_parent(a)  # a 의 루트 찾기
    root_b = find_parent(b)  # b 의 루트 찾기

    # 번호가 더 작은 루트 노드의 자식으로 더 큰 루트 노드 넣기
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b


arr_0 = []  # 사랑 안이루어진 관계 리스트, 판단해서 그래프에 추가
arr_1 = []  # 사랑 이루어진 관계 리스트, 무조건 그래프에 추가

# 입력 받아서 d 에 따라 arr_0, arr_1에 나누어 넣기
for i in range(m):
    a, b, c, d = map(int, input().split())
    if d == 1:  # 사랑 이루어진 관계는
        arr_1.append((a, b))  # 무조건 추가될거니까 필요한 a, b 만 담기
    else:  # 사랑 안이루어진 관계는
        heapq.heappush(arr_0, (-c, a, b))  # arr_0 에 -애정도, a, b 순으로 heappush()
                                           # -c 기준 오름차순으로 정렬된 상태를 유지하며 들어감
        # arr_0.append((-c, a, b))
        # 일단 집어넣고 나중에 한번에 heapify() 함수로 힙큐로 만들어주는 방식도 있지만 조금 더 느림

# heapq.heapify(arr_0)  # arr_0 에 append()로 넣어주었을 때 arr_0을 힙큐로 만들어주는 함수

# 사랑 이루어진 관계는 무조건 그래프에 추가하기
for a, b in arr_1:
    union_parent(a, b)

result = 0  # 포기시킨 애정도 합

# 사랑 안이루어진 관계는 판단해서 그래프에 추가하기
for i in range(len(arr_0)):
    cost, a, b = heapq.heappop(arr_0)  # heappop()으로 가장 작은 -cost(가장 큰 애정도) 가진 관계 꺼내기
    cost = -cost  # 애정도 다시 양수로 바꿔주기

    if find_parent(a) == find_parent(b):  # a, b 학생의 루트 노드가 동일하면 (== a, b 학생의 관계가 ?각 관계를 형성하면)
        result += cost  # 포기시킨 애정도에 이 관계의 애정도 추가

    else:  # ?각 관계를 형성하지 않으면
        union_parent(a, b)  # a, b 가 속한 트리의 루트노드 합치기 (== 그래프에 이 관계 추가하기)

print(result)  # 포기시킨 애정도 출력
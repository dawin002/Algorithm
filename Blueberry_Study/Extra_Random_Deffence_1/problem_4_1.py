import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 각 노드의 루트 노드 저장하는 parent 리스트
# 자기 자신을 루트로 가지는 초기 상태 설정
parent = [i for i in range(n + 1)]

# x 노드의 루트 노드 찾는 함수
def find_parent(x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]

# a, b 가 속한 트리를 합치는 함수
def union_parent(a, b):
    root_a = find_parent(a)
    root_b = find_parent(b)

    # 번호가 더 작은 루트 노드의 자식으로 더 큰 루트 노드 넣기
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

arr_0 = []
arr_1 = []

# 입력 받아서 d 에 따라 arr_0, arr_1에 나누어 넣기
for i in range(m):
    a, b, c, d = map(int, input().split())
    if d == 1:
        arr_1.append((a, b))
    else:
        # arr_0 에 (-애정도, a, b) 튜플 heappush()
        heapq.heappush(arr_0, (-c, a, b))
        # heappush()로 인해 -c 기준 오름차순으로 정렬된 상태를 유지하며 들어감

# 사랑 이루어진 관계는 무조건 그래프에 추가하기
for a, b in arr_1:
    union_parent(a, b)

result = 0  # 포기시킨 애정도 합

# 사랑 안이루어진 관계는 판단해서 그래프에 추가하기
for i in range(len(arr_0)):
    # heappop()으로 가장 작은 -cost(가장 큰 애정도) 가진 관계 꺼내기
    cost, a, b = heapq.heappop(arr_0)
    cost = -cost  # 애정도 다시 양수로 바꿔주기

    # ?각 관계(싸이클)를 형성하면 결과에 포기 애정도 추가
    if find_parent(a) == find_parent(b):
        result += cost
    else:  # 그렇지 않으면 a, b 가 속한 트리의 루트노드 합치기 (== 그래프에 추가)
        union_parent(a, b)

print(result)
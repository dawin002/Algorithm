import sys
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [i for i in range(n + 1)]

def find_parent(x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    root_a = find_parent(a)
    root_b = find_parent(b)
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
        arr_1.append((c, a, b))
    else:
        arr_0.append((c, a, b))

# 이미 이루어진 관계 그래프에 추가하기
for cost, a, b in arr_1:
    union_parent(a, b)

# 안이루어진 관계 cost 기준으로 내림차순 정렬
arr_0.sort(reverse=True, key=lambda x: x[0])

result = 0

# 안이루어진 관계는 싸이클 형성하는지 판단해서 그래프에 추가 / 포기 시키기
for cost, a, b in arr_0:
    if find_parent(a) == find_parent(b):
        result += cost
    else:
        union_parent(a, b)

print(result)
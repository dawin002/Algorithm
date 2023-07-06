import sys
input = sys.stdin.readline

# 학생 수, 관계 수 입력받기
n, m = map(int, input().split())

# 싸이클 형성 여부 판별용 리스트
# 각 노드(학생)가 속한 트리의 루트 노드 저장
parent = [i for i in range(n + 1)]  # 자기 자신을 루트로 가지는 초기 상태


# 싸이클 형성 여부 판별용 함수 1
# x 노드가 속한 트리의 루트 노드 찾는 함수
def find_parent(x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]


# 싸이클 형성 여부 판별용 함수 2
# a, b 가 속한 트리를 합치는 함수
def union_parent(a, b):
    root_a = find_parent(a)  # a 가 속한 트리의 루트 찾기
    root_b = find_parent(b)  # b 가 속한 트리의 루트 찾기

    # 번호가 더 큰 루트 노드를 더 작은 루트 노드의 자식으로 넣기
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
        arr_1.append((c, a, b))  # 무조건 추가하는 리스트에
    else:  # 사랑 안이루어진 관계는
        arr_0.append((c, a, b))  # 판단해서 추가하는 리스트에

# 이미 이루어진 관계 그래프에 추가하기
for cost, a, b in arr_1:
    union_parent(a, b)  # 각 학생이 속한 트리의 루트노드를 합침으로써 그래프상에서 연결됨

# 안이루어진 관계 cost 기준으로 내림차순 정렬
arr_0.sort(reverse=True, key=lambda x: x[0])

result = 0  # 포기시킨 애정도 합 (결과)

# 아직 안이루어진 관계는 싸이클 형성하는지 판단해서 그래프에 추가 / 포기 시키기
for cost, a, b in arr_0:
    # 두 학생의 루트 노드가 같다면 (싸이클 형성한다면)
    if find_parent(a) == find_parent(b):
        result += cost  # 결과값에 애정도 추가, 포기시켰다는 뜻
    else:  # 아니면
        union_parent(a, b)  # 두 학생이 속한 트리 합치기, 그래프에 추가했다는 뜻

print(result)  # 포기시킨 애정도 출력하기
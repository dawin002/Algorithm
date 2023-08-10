import sys
input = sys.stdin.readline

def recur(node, prv):
    # if parent[node] != -1: # 로 부모 체크 가능
    #     return

    # 부모로 부터 가져온 정보 다루기
    parent[node] = prv  # 부모 갱신

    # 재귀
    for nxt in tree[node]:
        # parent[nxt] = node # 로 부모 갱신 가능
        if nxt == prv:  # 부모 체크
            continue

        recur(nxt, node)

    # 자식으로부터 가져온 정보 다루기
    # child[prv] += 1 + child[node]

n = int(input())

tree = [[] for _ in range(n+1)]
parent = [-1 for _ in range(n+1)]
# child = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())

    tree[a].append(b)
    tree[b].append(a)

recur(1, 0)

for i in parent[2:]:
    print(i)
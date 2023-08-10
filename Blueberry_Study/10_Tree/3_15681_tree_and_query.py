import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def recur(node, prev):

    for nxt in tree[node]:
        if nxt == prev:
            continue

        recur(nxt, node)

    child[prev] += child[node]

n, r, q = map(int, input().split())

tree = [[] for _ in range(n+1)]
parent = [-1 for _ in range(n+1)]
child = [1 for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, input().split())

    tree[u].append(v)
    tree[v].append(u)

recur(r, 0)

for _ in range(q):
    print(child[int(input())])
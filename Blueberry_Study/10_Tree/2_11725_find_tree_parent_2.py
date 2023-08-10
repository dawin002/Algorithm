import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def recur(node, prv):

    parent[node] = prv

    for nxt in tree[node]:
        if nxt == prv:
            continue

        recur(nxt, node)

n = int(input())

tree = [[] for _ in range(n+1)]
parent = [-1 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())

    tree[a].append(b)
    tree[b].append(a)

recur(1, 0)

for i in parent[2:]:
    print(i)
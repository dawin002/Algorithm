""" 그래프 이론 : 2. 팀 결성 """

# 학생 번호 0 ~ N
# 처음엔 모두 다른팀 --> N+1개 팀
# 연산 1. 팀 합치기 : 두 팀합침
# 연산 2. 같은 팀 여부 확인 : 특정 두 학생 같은 팀인지 확인
# M개의 연산 수행할 수 있을 때 같은팀확인연산 연산결과 출력

def makeTeam():
    n, m = map(int, input().split())
    orders = [tuple(map(int, input().split())) for _ in range(m)]
    parent = [0] * (n+1)
    for i in range(1, n+1):
        parent[i] = i

    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    def union(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    def check_team(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a == b:
            return 'YES'
        else:
            return 'NO'

    for order in orders:
        o, a, b = order
        if o == 0:
            union(parent, a, b)
        elif o == 1:
            ans = check_team(parent, a, b)
            print(ans)

makeTeam()

# input
# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1
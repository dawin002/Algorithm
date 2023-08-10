""" 그래프 이론 문제 : 45. 최종 순위 """

# n 개 팀 (1~n번) <= 500
# 작년 순위 제공
# 올해는 제공 안함
# 작년에 비해 상대 순위가 뒤바뀐 두 팀 번호 쌍 제공 <= 25,000
# 올해 순위 1등부터 한 줄에 출력
# 순위 나오는 경우의 수 여러 개라면 ? 출력
# 어떤 순위도 나올 수 없다면 INPOSSIBLE 출력

""" my code : 풀이 방식 보고 코드는 내가 짬 """

# 핵심 아이디어 : 정해진 우선순위에 맞게 전체 팀 순위 나열
#             == 위상 정렬 알고리즘
#                (팀간 순위 정보 그래프로 표현 후 위상 정렬 알고리즘 수행)
# 풀이 방식
# 1. 작년 순위 정보로 자신보다 낮은 팀 가리키는 그래프 만들기
# 2. 상대 순위 뒤바뀐 두 팀 가리키는 방향 반대로 하기
# 3. 위상 정렬 수행
#    참고 1. 일반적인 위상 정렬의 경우 노드가 N개라면 N개의 노드가 큐에서 출력
#    참고 2. 특정 시점에 2개 이상의 노드가 큐에 들어가면 가능한 정렬 결과가 여러개라는 뜻
# 4. 위상 정렬 반복문 돌며 큐의 원소 개수 체크
#    1) 큐의 원소가 1개로 유지되면(진입차수가 0인 원소 1개로 유지) 최종 순위 출력
#    2) 큐의 원소가 2개 이상이면(진입차수 0인 원소 2개 이상 == 여러 정렬 결과 존재) 정확한 순위 알 수 없음
#    3) N개의 원소가 뽑히기 전 큐의 원소가 없으면(진입차수 0인 원소 0개 == 사이클 존재) 잘못된 데이터

# 내 풀이 책 풀이와 다른점 : 그래프 표현 방식
# 내 풀이 : 인접 리스트로 연결된 간선만 표현
# 책 풀이 : 2차원 행렬 리스트로 전체 그래프 표현

def final_ranking_hint():
    import sys
    from collections import deque

    n = int(sys.stdin.readline())
    pre_rank = list(map(int, sys.stdin.readline().split()))

    indegree = [0] * (n+1)
    edges = [set() for _ in range(n+1)]

    for i in range(n):
        for j in range(i+1, n):
            edges[pre_rank[i]].add(pre_rank[j])

    m = int(sys.stdin.readline())
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        if b in edges[a]:
            edges[a].remove(b)
            edges[b].add(a)
        else:
            edges[b].remove(a)
            edges[a].add(b)

    for i in range(1, n+1):
        for b in edges[i]:
            indegree[b] += 1

    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    result = []

    for _ in range(n):
        if len(q) == 0:
            return 'IMPOSSIBLE'
        if len(q) > 1:
            return '?'
        now = q.popleft()
        result.append(now)
        for b in edges[now]:
            indegree[b] -= 1
            if indegree[b] == 0:
                q.append(b)

    return ' '.join(map(str, result))


""" answer code """

def final_ranking_ans():
    import sys
    from collections import deque

    n = int(sys.stdin.readline())
    # 모든 노드에 대한 진입차수 0 초기화
    indegree = [0] * (n+1)
    # 각 노드에 연결된 간선 정보 담기 위한 인접 행렬 초기화
    graph = [[False] * (n+1) for _ in range(n + 1)]
    # 작년 순위 정보 입력
    data = list(map(int, sys.stdin.readline().split()))
    # 방향 그래프의 간선 정보 초기화
    for i in range(n):
        for j in range(i+1, n):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1

    # 올해 변경된 순위 정보 입력
    m = int(sys.stdin.readline())
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        # 입력받은 a->b 그래프에 없다면 swap(a,b)
        if not graph[a][b]:
            a, b = b, a
        # a->b ==> b->a 로 간선 방향 뒤집기
        graph[a][b] = False
        graph[b][a] = True
        indegree[b] -= 1
        indegree[a] += 1

    # 위상 정렬 시작
    result = []  # 알고리즘 수행 결과
    q = deque()  # 큐
    # 진입차수가 0인 노드 모두 큐에 삽입
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    certain = True  # 위상 정렬 결과 오직 하나인가?
    cycle = False   # 사이클이 존재하는가?

    # 정확히 노드의 개수만큼 반복 (위상 정렬이 노드 개수만큼 큐에서 나오기 때문에)
    for _ in range(n):
        # 큐가 비어있다면 사이클 발생했다는 뜻
        if len(q) == 0:
            cycle = True
            break
        # 큐의 원소가 2개 이상이면 가능한 정렬 결과가 여러개라는 뜻
        if len(q) > 1:
            certain = False
            break
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드의 진입차수에서 1 감소
        for j in range(1, n+1):
            if graph[now][j]:
                indegree[j] -= 1
                # 새롭게 진입차수 0이 된 노드 큐에 추가
                if indegree[j] == 0:
                    q.append(j)

    # 사이클이 발생했다면(데이터 일관성 없음)
    if cycle:
        print("IMPOSSIBLE")
    # 위상 정렬 결과가 하나가 아니라면(정확한 순위 알 수 없음)
    elif not certain:
        print("?")
    # 위상 정렬 수행한 결과 출력
    else:
        print(' '.join(map(str, result)))


def solution():
    for test_case in range(int(input())):
        # ans = final_ranking_hint()
        final_ranking_ans()

solution()

# input
# 3
# 5
# 5 4 3 2 1
# 2
# 2 4
# 3 4
# 3
# 2 3 1
# 0
# 4
# 1 2 3 4
# 3
# 1 2
# 3 4
# 2 3


# output
# 5 3 2 4 1
# 2 3 1
# IMPOSSIBLE
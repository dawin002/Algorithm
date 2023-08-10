""" 그래프 이론 : 4.커리큘럼 """

# 시작 시간: 1705
# 풀이 시간: 50분
# 마감 시간: 1755

# 선수강의 전부 들어야 후수강의 수강 가능
# 1~N번까지 강의 있음
# 동시에 여러개 강의 들을 수 있음
#
# 1번 = 30시간
# 2번 = 20시간
# 3번 = 40시간
# 3번 선수강의 1,2번일때
# --> 3번까지 듣는데 총 40시간
#
# 첫째 줄 : 듣고자하는 강의 수 N (1<=N<=500)
# N개 줄 : 각 강의 시간, 선수강의들, -1(끝 표시) (강의시간<10만)
#
# 출력 : 첫강부터 각 강의까지 듣는데 걸리는 최소 시간

def new_solution():
    import copy
    from collections import deque
    n = int(input())
    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    time = [0] * (n+1)
    for i in range(1, n+1):
        cost, *a_lst = map(int, input().split())
        time[i] = cost
        a_lst.pop()
        indegree[i] = len(a_lst)
        for b in a_lst:
            graph[b].append(i)

    q = deque()
    print(graph)

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    # res_time = [t for t in time]
    res_time = copy.deepcopy(time)

    while q:
        now = q.popleft()
        for i in graph[now]:
            res_time[i] = max(res_time[now] + time[i], res_time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for r in res_time[1:]:
        print(r)

new_solution()




def curriculum_ans():
    from collections import deque
    import copy

    # 노드의 개수 입력받기
    v = int(input())

    # 모든 노드에 대한 진입차수는 0으로 초기화
    indegree = [0] * (v+1)
    # 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
    graph = [[] for _ in range(v+1)]
    # 각 강의 시간을 0으로 초기화
    time = [0] * (v+1)

    # 방향 그래프의 모든 간선 정보를 입력받기
    for i in range(1, v+1):
        t, *fclst = map(int, input().split())
        fclst.pop()
        time[i] = t
        indegree[i] = len(fclst)
        for fc in fclst:
            graph[fc].append(i)

    print(graph)

    # 위상 정렬 함수
    def topology_sort():
        q = deque()
        # 알고리즘 수행 결과를 담을 리스트에 time 리스트 복사하기
        result = copy.deepcopy(time)

        # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
        for i in range(1, v+1):
            if indegree[i] == 0:
                q.append(i)

        # 큐가 빌 때까지 반복
        while q:

            # 큐에서 원소 꺼내기
            now = q.popleft()

            for node in graph[now]:
                # ???
                result[node] = max(result[node], result[now]+time[node])
                # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
                indegree[node] -= 1

                # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                if indegree[node] == 0:
                    q.append(node)

        # 위상 정렬을 수행한 결과 출력
        for i in range(1, v+1):
            print(result[i])

    topology_sort()

curriculum_ans()

# input
# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1



def curriculum_ans_print():
    from collections import deque
    import copy

    v = 5
    input_text = [[10, -1], [10, 1, -1], [4, 1, -1], [4, 3, 1, -1], [3, 3, -1]]
    indegree = [0] * (v+1)
    graph = [[] for _ in range(v+1)]
    time = [0] * (v+1)

    for i in range(1, v+1):
        t, *fclst = input_text[i-1]
        fclst.pop()
        time[i] = t
        indegree[i] = len(fclst)
        for fc in fclst:
            graph[fc].append(i)

    def topology_sort():
        q = deque()
        result = copy.deepcopy(time)

        print('=================================')
        print('q   :', *q)
        print('ind :', indegree[1:])
        print('res :', result[1:])

        for i in range(1, v+1):
            if indegree[i] == 0:
                q.append(i)

        while q:
            print('=================================')
            print('q   :', *q)
            now = q.popleft()
            print(f'q.popleft = {now}')
            print(f'SunSoo[{now}] : {graph[now]}')
            for node in graph[now]:
                print('----------------------')
                print(f'res[{node}] = max(res{[node]}, res{[now]}+time{[node]})')
                result[node] = max(result[node], result[now]+time[node])
                print(f'ind[{node}] -= 1')
                indegree[node] -= 1
                print('ind :', indegree[1:])
                print('res :', result[1:])
                if indegree[node] == 0:
                    q.append(node)
                    print(f'q.append({node})')

        print('=================================')
        for i in range(1, v+1):
            print(result[i])

    topology_sort()

# curriculum_ans_print()
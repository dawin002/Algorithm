""" 최단 경로 문제 : 숨바꼭질 """

# 1~n번 n개 집
# 술래 1번 시작
# m개의 양방향 통로
# 1번으로부터 최단거리 가장 먼 집 출력

""" my solution """

# 다익스트라 알고리즘 잘못 구현
# 1. 큐에 뭘 넣을지 틀림
#    큐에 넣어야 하는 튜플은 (거리, 도착 지점)인데 도착 지점은 다음 번에 큐에서 꺼내지면 시작 지점으로 사용됨
# 2. 큐에서 꺼낸 후 꺼낸 튜플의 dist 보다 distance[end] 가 더 작으면 이미 처리된 노드이므로 건너뛰어라
#    라는 코드 안넣음 --> 시간복잡도 엄청 증가

def hide_and_seek():
    import heapq
    INF = int(1e9)
    n, m = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        # graph[출발 노드] 에 (비용 1, 도착 노드) 추가 : 양방향이므로 반대로도 추가
        graph[a].append((1, b))
        graph[b].append((1, a))

    distance = [INF] * (n + 1)
    distance[1] = 0
    start = 1

    q = []
    heapq.heappush(q, (distance[start], start))

    while q:
        # now : 현재 노드, dist : 현재 노드까지 가는 최단거리
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 노드이므로 건너뛰어라
        if distance[now] < dist:
            continue
        # 현재 노드로부터 갈 수 있는 노드와 거리 하나씩 받기
        for one in graph[now]:
            cost, end = one
            # distance 에 저장된 start 에서 end 로 가는 비용보다 now 를 들렀다 가는 비용
            # now 들리는 비용 = start->now + now->end = dist + cost
            if distance[end] > dist + cost:
                distance[end] = dist + cost
                heapq.heappush(q, (dist + cost, end))

    # 1부터 출발하는 최단 경로 가장 큰 노드 구하기
    max_node = 0
    max_dist = 0
    max_dist_count = 1
    for i in range(1, n+1):
        if distance[i] > max_dist:
            max_node = i
            max_dist = distance[i]
            max_dist_count = 1
        elif distance[i] == max_dist:
            max_dist_count += 1

    print(max_node, max_dist, max_dist_count)

hide_and_seek()


# 입력
# 6 7
# 3 6
# 4 3
# 3 2
# 1 3
# 1 2
# 2 4
# 5 2

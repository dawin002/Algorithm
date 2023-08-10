""" 최단 경로 문제 : 37. 플로이드 """

# n 개의 도시
# m 개의 경로
# 각 경로 다른 비용
# 모든 도시 쌍 비용 최솟값 구하기

""" my solution : 힌트 봄 ( 플로이드 워셜 알고리즘 ), 틀림 """

# 힌트 : 플로이드 워셜 알고리즘
# 중첩 for 문 3개 돌려야 함
# for k in range(1, n+1) : # 경유할 k 도시 하나 지정 해두기
#   for i in range(1, n+1):
#       for j in range(1, n+1): # 모든 graph[i][j]에 대해 k 도시를 들렀다 가면 더 빠른지 확인

# 틀린 것 : 입력되는 경로 중 출발지, 목적지 같지만 비용 더 큰 경로 있었는데 처리 안해줬음

def floyd():
    INF = int(1e9)
    n = int(input())
    m = int(input())
    g = [[INF] * (n + 1) for _ in range(n + 1)]

    # 자기 자신에게 가는 경로 비용 0 처리
    for i in range(n + 1):
        g[i][i] = 0

    # 입력받은 경로 그래프에 저장 (원래 저장된 비용보다 크면 무시)
    for _ in range(m):
        a, b, c = map(int, input().split())
        if c < g[a][b]:
            g[a][b] = c

    # 플로이드 워셜 알고리즘으로 최단 경로 구하기
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])

    # 출력
    for i in range(1, n+1):
        for j in range(1, n+1):
            if g[i][j] == INF:
                print('0', end=' ')
            else:
                print(g[i][j], end=' ')
        print()

floyd()


# input1
# 5
# 14
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 3 5 10
# 3 1 8
# 1 4 2
# 5 1 7
# 3 4 2
# 5 2 4
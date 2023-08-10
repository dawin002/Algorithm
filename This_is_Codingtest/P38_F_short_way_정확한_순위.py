""" 최단 경로 문제 : 38. 정확한 순위 """

# n 명의 학생
# (a 학생 성적 < b 학생 성적) 쌍의 순위만 제공
# a < b 이면 a --> b 화살표로 표시
# 정확하게 순위 알 수 있는 학생 몇 명인지 출력

""" answer solution (변형) : 플로이드 워셜 알고리즘 변형 """

# 배워야 할 것
# 플로이드 워셜 알고리즘 기반 풀이 방식
# 특정 학생이 다른 모든 학생과 연결되어 있으면 그 학생의 순위 알 수 있음!
# 연결 되어 있다 확인법 : 각 학생에 대해 출발점 or 도착점 중 하나라도 INF가 아니다.

def accurate_rank_ans2():
    n, m = map(int, input().split())
    g = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n+1):
        g[i][i] = 1

    for _ in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if g[i][k] == g[k][j] == 1:
                    g[i][j] = 1

    result = 0
    for i in range(1, n+1):
        count = 0
        for j in range(1, n+1):
            if g[i][j] == 1 or g[j][i] == 1:
                count += 1
        if count == n:
            result += 1

    print(result)

    s = '123456'
    c = 0
    print('   ', *list(s))
    for i in g[1:]:
        print(s[c], '[', end=' ')
        c += 1
        for j in i[1:]:
            if j == 0:
                print('.', end=' ')
            else:
                print('O', end=' ')
        print(']')

accurate_rank_ans2()

""" answer code : 플로이드 워셜 알고리즘 오리지널 """
def accurate_rank_ans():
    INF = int(1e9)
    n, m = map(int, input().split())
    g = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n+1):
        g[i][i] = 0

    for _ in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])

    result = 0
    for i in range(1, n+1):
        count = 0
        for j in range(1, n+1):
            if g[i][j] != INF or g[j][i] != INF:
                count += 1
        if count == n:
            result += 1

    print(result)

    s = '123456'
    c = 0
    print('   ', *list(s))
    for i in g[1:]:
        print(s[c], '[', end=' ')
        c += 1
        for j in i[1:]:
            if j == INF:
                print('.', end=' ')
            else:
                print('o', end=' ')
        print(']')

accurate_rank_ans()


# input
# 6 6
# 1 5
# 3 4
# 4 2
# 4 6
# 5 2
# 5 4
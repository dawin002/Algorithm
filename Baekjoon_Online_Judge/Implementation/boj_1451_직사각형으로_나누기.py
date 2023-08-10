""" 1451 : 직사각형으로 나누기 """

# 문제
# 세준이는 N*M크기로 직사각형에 수를 N*M개 써놓았다.

# 세준이는 이 직사각형을 겹치지 않는 3개의 작은 직사각형으로 나누려고 한다. 각각의 칸은 단 하나의 작은 직사각형에 포함되어야 하고, 각각의 작은 직사각형은 적어도 하나의 숫자를 포함해야 한다.

# 어떤 작은 직사각형의 합은 그 속에 있는 수의 합이다. 입력으로 주어진 직사각형을 3개의 작은 직사각형으로 나누었을 때, 각각의 작은 직사각형의 합의 곱을 최대로 하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 직사각형의 세로 크기 N과 가로 크기 M이 주어진다. 둘째 줄부터 직사각형에 들어가는 수가 가장 윗 줄부터 한 줄에 하나씩 M개의 수가 주어진다. N과 M은 50보다 작거나 같은 자연수이고, 직사각형엔 적어도 3개의 수가 있다. 또, 직사각형에 들어가는 수는 한 자리의 숫자이다.

# 출력
# 세 개의 작은 직사각형의 합의 곱의 최댓값을 출력한다.

""" my code failed """

# 0. 직사각형인지 판단하는 함수 만든다
# 1. 직사각형으로 나누는 규칙 찾는다
# 2. 나눈 세 값 직사각형이면 패스, 아니면 버림
# 2. 세 직사각형 차이 제일 적게 나는 값 찾는다
# 3.

# 직사각형 나누는 방식
# 1번 직사각형 선택
# 1번 직사각형 선택하는 방식
# row 따라서 반복 하면서 col 따라서 반복
# rs 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# re 0 0 0 0 0 1 1 1 1 1 2 2 2 2 2
# cs 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# ce 0 1 2 3 4 0 1 2 3 4 0 1 2 3 4
# 그 뒤 2번, 3번 나눔
# 2, 3번 직사각형은 re, ce가 끝이 아닐때는 두가지 방법으로 나뉨
# 2번이 남은 col을 먹을건지, 남은 row를 먹을건지
# re나 ce가 끝에 도달했을 때는 세로로 나눌건지, 가로로 나눌건지

# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1

#
""" answer code """


def recTo3_ans():
    import sys

    n, m = map(int, sys.stdin.readline().split())
    table = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
    ans = 0

    # |||
    for i in range(1, m - 1):
        for j in range(i + 1, m):
            s1 = sum([table[a][b] for a in range(n) for b in range(i)])
            s2 = sum([table[a][b] for a in range(n) for b in range(i, j)])
            s3 = sum([table[a][b] for a in range(n) for b in range(j, m)])
            ans = max(ans, s1 * s2 * s3)

    # -
    # -
    # -
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            s1, s2, s3 = 0, 0, 0
            for a in range(i): s1 += sum(table[a])
            for a in range(i, j): s2 += sum(table[a])
            for a in range(j, n): s3 += sum(table[a])
            # s1 = sum([table[a][b] for a in range(i) for b in range(m)])
            # s2 = sum([table[a][b] for a in range(i, j) for b in range(m)])
            # s3 = sum([table[a][b] for a in range(j, n) for b in range(m)])
            ans = max(ans, s1 * s2 * s3)

    # ||
    # --
    for i in range(1, m):
        for j in range(1, n):
            s1 = sum([table[a][b] for a in range(j) for b in range(i)])
            s2 = sum([table[a][b] for a in range(j) for b in range(i, m)])
            s3 = sum([table[a][b] for a in range(j, n) for b in range(m)])
            ans = max(ans, s1 * s2 * s3)

    # --
    # ||
    for i in range(1, n):
        for j in range(1, m):
            s1 = sum([table[a][b] for a in range(i) for b in range(m)])
            s2 = sum([table[a][b] for a in range(i, n) for b in range(j)])
            s3 = sum([table[a][b] for a in range(i, n) for b in range(j, m)])
            ans = max(ans, s1 * s2 * s3)

    # =|
    for i in range(1, n):
        for j in range(1, m):
            s1 = sum([table[a][b] for a in range(i) for b in range(j)])
            s2 = sum([table[a][b] for a in range(i, n) for b in range(j)])
            s3 = sum([table[a][b] for a in range(n) for b in range(j, m)])
            ans = max(ans, s1 * s2 * s3)

    # |=
    for i in range(1, n):
        for j in range(1, m):
            s1 = sum([table[a][b] for a in range(i) for b in range(j, m)])
            s2 = sum([table[a][b] for a in range(i, n) for b in range(j, m)])
            s3 = sum([table[a][b] for a in range(n) for b in range(j)])
            ans = max(ans, s1 * s2 * s3)

    print(ans)
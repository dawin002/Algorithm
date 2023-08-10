""" 1931 : 회의실 배정 """

# 한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다.
# 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자.
# 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
# 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.

# 입력
# 첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다.
# 둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다.
# 시작 시간과 끝나는 시간은 (2^31)-1보다 작거나 같은 자연수 또는 0이다.

# 출력
# 첫째 줄에 최대 사용할 수 있는 회의의 최대 개수를 출력한다.

#
""" my code """


def meetingRoom2():
    import sys
    t = []
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        t.append((a, b, b - a))

    t.sort(key=lambda x: x[1])
    latest = t[-1][1]
    print(latest)

    t.sort(key=lambda x: (x[2], x[0]))
    print('t', t)

    time = [0 for _ in range(latest + 1)]
    print(time)
    count = 0
    for i in t:
        if sum(time[i[0]:i[1]]) == 0:
            print(i[0], i[1])
            if i[0] == i[1]:
                time[i[0]] = 1
            else:
                for j in range(i[1] - i[0]):
                    time[i[0] + j] = 1
            count += 1
            print(time)
    print(count)

    # 1 2
    # 4 5
    # 2 4

    # 1 2 3 4 5 6 7 8 9
    # 0 0 0 0 0 0 0 0 0
    # 1 0 0 1 1 0 0 0 0


""" my code 2 : (힌트 : 빨리 끝나는 순으로 정렬해봐라) """


def meetingroom3():
    import sys
    n = int(sys.stdin.readline().rstrip())
    t = []
    for _ in range(n):
        t.append(tuple(map(int, sys.stdin.readline().split())))
    t.sort(key=lambda x: (x[1], x[0]))

    last = t[0][1]
    count = 1
    # print('t[i] =', t[0], ', last =', last, ', count =', count)
    for i in range(1, n):
        if last <= t[i][0]:
            last = t[i][1]
            count += 1
            # print('t[i] =', t[i], ', last =', last, ', count =', count)
    print(count)


""" another way """


def meetingroom_ans1():
    import sys
    input = sys.stdin.readline
    n = int(input())
    table = []
    for i in range(n) :    # 윗줄이랑 동일 문장
      table.append( (*map(int, input().split(' ')), ) )
    table.sort()
    count, last = 0, float('inf')
    for a, b in reversed(table):
        if b <= last:
            last = a
            count += 1
    print(count)


""" map test """


def map_test():
    import sys
    n = int(input())
    t = []
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        t.append((a, b))
    print(t)


""" another way """


def meetingroom_ans2():
    import sys
    In = sys.stdin
    n = int(input())
    time = [tuple(map(int, In.readline().split(' '))) for _ in range(n)]
    time.sort(key=lambda x: (x[1], x[0]))
    ans = end = 0
    for s, e in time:
        if s >= end:
            ans += 1
            end = e
    print(ans)

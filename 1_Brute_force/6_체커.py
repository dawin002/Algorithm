""" 체커 """

def checker():
    n = int(input())

    coordinates = []
    x_list = []
    y_list = []
    ans = [int(1e9)] * n
    ans[0] = 0
    for _ in range(n):
        a, b = map(int, input().split())
        coordinates.append((a, b))
        x_list.append(a)
        y_list.append(b)

    for y in y_list:
        for x in x_list:
            dist = []
            for ex, ey in coordinates:
                d = abs(ex-x) + abs(ey-y)
                dist.append(d)

            dist.sort()
            for i in range(1, n):
                dist[i] += dist[i-1]
                if dist[i] < ans[i]:
                    ans[i] = dist[i]

    print(*ans)

# checker()


def checker_2():
    n = int(input())

    coordinates = []
    x_list = []
    y_list = []
    ans = [int(1e9)] * n
    ans[0] = 0
    for _ in range(n):
        a, b = map(int, input().split())
        coordinates.append((a, b))
        x_list.append(a)
        y_list.append(b)

    for y in y_list:
        for x in x_list:
            dist = []
            for ex, ey in coordinates:
                d = abs(ex-x) + abs(ey-y)
                dist.append(d)

            dist.sort()
            for i in range(1, n):
                dist[i] += dist[i-1]
                if dist[i] < ans[i]:
                    ans[i] = dist[i]

    print(*ans)

checker_2()
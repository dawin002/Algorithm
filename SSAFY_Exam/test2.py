


# T = int(input())

for test_case in range(1, 2):
    from collections import deque
    n, y = map(int, input().split())
    arr = deque([tuple(map(int, input().split())) for _ in range(n)])
    x = 0
    x_time = 0
    y_time = 0
    x_left = 0
    y_left = 0

    while arr:
        if x >= y:
            print(x, y)
            break
        if x_time == x_left == 0 and arr:
            x_stop, x_time = arr.popleft()
            x_left = x_stop - x
        if y_time == y_left == 0 and arr:
            y_stop, y_time = arr.pop()
            y_left = y - y_stop

        if x_time == y_time == 0:
            if x_left <= y_left:
                x += x_left
                y -= x_left
                y_left -= x_left
            else:
                y -= y_left
                x += y_left
                x_left -= y_left
        else:
            if x_time == y_time:
                x_time = 0
                y_time = 0
            elif x_time < y_time:
                y_time -= x_time
                x_time = 0
            else:
                x_time -= y_time
                y_time = 0

    print(x)




# 9
# 1 10
# 8 2
# 3 100
# 2 2
# 4 2
# 6 2
# 3 100
# 2 2
# 50 2
# 98 4
# 1 10
# 4 118
# 1 100
# 46 68
# 1 10000
# 5000 50
# 10 1000
# 14 100
# 34 186
# 40 104
# 174 54
# 216 128
# 218 120
# 298 10
# 358 124
# 624 192
# 686 162
# 11 1000
# 38 166
# 98 54
# 268 2
# 274 44
# 400 20
# 608 40
# 692 82
# 704 114
# 756 38
# 818 32
# 872 8
# 12 10000
# 768 154
# 1538 146
# 2306 168
# 3076 86
# 3844 118
# 4614 126
# 5382 122
# 6152 28
# 6920 108
# 7690 148
# 8458 26
# 9228 144

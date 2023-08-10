import sys
import heapq

input = sys.stdin.readline

dimensions = list(map(int, input().split()))

D_SIZE = len(dimensions)

direction = [[0 for _ in range(D_SIZE)] for _ in range(D_SIZE * 2)]
for i in range(D_SIZE):
    direction[i][i] = 1
    direction[D_SIZE + i][i] = -1

zero_count = 0
queue = []
position = []


def recur_make_map(idx):
    if idx == D_SIZE:
        global zero_count
        line = list(map(int, input().split()))
        for j in range(len(line)):
            if line[j] == 1:
                position.append(j)
                queue.append((1, *position))
                position.pop()
            elif line[j] == 0:
                zero_count += 1
        return line
    tmp = []
    for i in range(dimensions[-idx]):
        position.append(i)
        tmp.append(recur_make_map(idx + 1))
        position.pop()
    return tmp


def get_tomato_value(tmp_list, idx):
    if idx == D_SIZE - 1:
        return tmp_list[nxt_pos[idx]]
    return get_tomato_value(tmp_list[nxt_pos[idx]], idx + 1)


def set_tomato_value(tmp_list, idx, value):
    if idx == D_SIZE - 1:
        tmp_list[nxt_pos[idx]] = value
        return
    set_tomato_value(tmp_list[nxt_pos[idx]], idx + 1, value)


tomato_map = recur_make_map(1)

# print(tomato_map)
# print(queue)

heapq.heapify(queue)

# print('queue')
# for line in queue:
#     print(line)

while queue:
    day, *now_pos = heapq.heappop(queue)
    for dir_pos in direction:
        nxt_pos = [now_pos[i] + dir_pos[i] for i in range(len(dir_pos))]
        is_pos_in_range = True
        for i in range(D_SIZE):
            if not (0 <= nxt_pos[i] < dimensions[::-1][i]):
                is_pos_in_range = False
                break
        if not is_pos_in_range:
            continue
        if get_tomato_value(tomato_map, 0) != 0:
            continue
        zero_count -= 1
        set_tomato_value(tomato_map, 0, day + 1)
        heapq.heappush(queue, (day + 1, *nxt_pos))

# print(tomato_map)

if zero_count != 0:
    print(-1)
else:
    print(day - 1)
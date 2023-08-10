from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque()
length = 0

while True:
    tmp = int(input())
    if tmp == -1:
        break
    elif tmp == 0:
        if length != 0:
            queue.popleft()
            length -= 1
    else:
        if length < n:
            queue.append(tmp)
            length += 1

if length != 0:
    print(*queue)
else:
    print('empty')

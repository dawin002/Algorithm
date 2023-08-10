from collections import deque
import heapq
from itertools import permutations
from itertools import combinations

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
queue.append(6)

print(queue)

queue.popleft()
queue.popleft()
queue.popleft()

queue = list(queue)

for per in permutations(queue, 2):
    print(per, end=' ')
print()

for com in combinations(queue, 2):
    print(com, end=' ')
print()

queue.pop()
queue.pop()
queue.pop()

heapq.heappush(queue, 5)
heapq.heappush(queue, 7)
heapq.heappush(queue, 1)
heapq.heappush(queue, 3)
heapq.heappush(queue, 9)
while queue:
    print(heapq.heappop(queue), end=' ')
print()

import platform

print(platform.python_implementation())
print(platform.python_version())
n = int(input())

mmap = [[0] * 120 for _ in range(120)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            mmap[x + i][y + j] = 1

count = 0

for i in range(100):
    for j in range(100):
        if mmap[i][j] != 0:
            count += 1

print(count)
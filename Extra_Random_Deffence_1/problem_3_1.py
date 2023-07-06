import sys
input = sys.stdin.readline

sina_x, sina_y, n = map(int, input().split())
sina_x += 500
sina_y += 500

mmap = [[0 for _ in range(1001)] for _ in range(1001)]

for i in range(n):
    tmp_x, tmp_y = map(int, input().split())
    mmap[tmp_x + 500][tmp_y + 500] = -1
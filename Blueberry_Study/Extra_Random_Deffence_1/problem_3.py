# 일단 좌표 헷갈리니까
# x 좌표 중 최소값이 음수면 0이 되게 모든 좌표에 abs(x)만큼 더해주기
# y 좌표 중 최소값이 음수면 0이 되게 모든 좌표에 abs(y)만큼 더해주기
# 신아 위치인 (X, Y)와 출발 위치 (0, 0)에 abs(x), abs(y) 각각 더해주기

# 2차원 맵 만들어서 웅덩이 위치 표시하기

# bfs로 웅덩이가 없는 좌표마다 시작점에서부터 갈 수 있는 걸음 수 최소값 적어주기

# 신아 위치 도달하면 신아 위치에 있는 숫자 출력

import sys
input = sys.stdin.readline

sina_x, sina_y, n = map(int, input().split())
min_x, min_y = -1, -1
max_x, max_y = -999999999999, -99999999999

water = []

for i in range(n):
    tmp_x, tmp_y = map(int, input().split())
    min_x = min(min_x, tmp_x)
    min_y = min(min_y, tmp_y)
    max_x = max(max_x, tmp_x)
    max_y = max(max_y, tmp_y)
    water.append([tmp_x, tmp_y])

sina_x -= min_x
sina_y -= min_y

for i in range(n):
    water[i][0] -= min_x
    water[i][1] -= min_y
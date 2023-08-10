""" 예제 4-1 상하좌우 """
# page 110

#
""" my code """


def UpDownLeftRight():
  import sys
  input = sys.stdin.readline

  end = int(input().rstrip())
  map_x = 1
  map_y = 1
  go = list(input().rstrip().split())

  for i in go:
    if i == 'U':
      if map_y > 1:
        map_y -= 1
    elif i == 'D':
      if map_y < end:
        map_y += 1
    elif i == 'L':
      if map_x > 1:
        map_x -= 1
    elif i == 'R':
      if map_x < end:
        map_x += 1

  print(map_y, map_x)


""" answer """


def UpDownLeftRight_ans():
  n = int(input())
  x, y = 1, 1
  plans = input().split()

  dx = [0, 0, -1, 1]
  dy = [-1, 1, 0, 0]
  move_types = ['U', 'D', 'L', 'R']

  for plan in plans:
    for i in range(len(move_types)):
      if plan == move_types[i]:
        nx = x + dx[i]
        ny = y + dy[i]
    if 1 <= nx <= n and 1 <= ny <= n:
      x, y = nx, ny

  print(x, y)
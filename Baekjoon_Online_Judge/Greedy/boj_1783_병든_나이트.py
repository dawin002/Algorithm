""" 1783 : 병든 나이트 """

# 병든 나이트가 N × M 크기 체스판의 가장 왼쪽아래 칸에 위치해 있다. 병든 나이트는 건강한 보통 체스의 나이트와 다르게 4가지로만 움직일 수 있다.

# 2칸 위로, 1칸 오른쪽
# 1칸 위로, 2칸 오른쪽
# 1칸 아래로, 2칸 오른쪽
# 2칸 아래로, 1칸 오른쪽
# 병든 나이트는 여행을 시작하려고 하고, 여행을 하면서 방문한 칸의 수를 최대로 하려고 한다. 병든 나이트의 이동 횟수가 4번보다 적지 않다면, 이동 방법을 모두 한 번씩 사용해야 한다. 이동 횟수가 4번보다 적은 경우(방문한 칸이 5개 미만)에는 이동 방법에 대한 제약이 없다.

# 체스판의 크기가 주어졌을 때, 병든 나이트가 여행에서 방문할 수 있는 칸의 최대 개수를 구해보자.

# 입력
# 첫째 줄에 체스판의 세로 길이 N와 가로 길이 M이 주어진다. N과 M은 2,000,000,000보다 작거나 같은 자연수이다.

# 출력
# 병든 나이트가 여행에서 방문할 수 있는 칸의 개수중 최댓값을 출력한다.

#
""" my code """

# 나이트 위치 : n-1, 0
# 나이트 4방향 다 이동 : 세로로 0, 오른쪽으로 +6
# 오른쪽으로 최대한 덜가는 법 : 2위1오 -> 2아1오


def sickKnight():
  n, m = map(int, input().split())
  chessMap = [['0' for _ in range(m)] for _ in range(n)]
  nowNM = [n - 1, 0]
  moveNM = [0, 0]
  setKnight(nowNM, chessMap)
  printMap(chessMap, nowNM)
  while True:
    print('1:2U1R, 2:1U2R, 3:1D2R, 4:2D1R \n>> input:', end='')
    move = int(input())
    print()
    moveNM = setMove(move)
    if moveNM[0] == moveNM[1] == -1:
      print('Sick Knight End')
      break
    moveKnight(nowNM, moveNM, chessMap)
    printMap(chessMap, nowNM)


# sickKnight 내장 함수 : 나이트 처음 위치 설정
def setKnight(nowNM, chessMap):
  chessMap[nowNM[0]][nowNM[1]] = 1


# sickKnight 내장 함수 : 나이트 움직이기
def moveKnight(nowNM, moveNM, chessMap):
  if cantMove(nowNM, moveNM, chessMap) == True:
    return
  else:
    chessMap[nowNM[0]][nowNM[1]] = 0
    nowNM[0] -= moveNM[0]
    nowNM[1] += moveNM[1]
    chessMap[nowNM[0]][nowNM[1]] = 1


# sickKnight 내장 함수 : 나이트 움직일 좌표 계산하기
def setMove(move):
  if move == 1: return 2, 1
  elif move == 2: return 1, 2
  elif move == 3: return -1, 2
  elif move == 4: return -2, 1
  else: return -1, -1


# sickKnight 내장 함수 : 나이트 움직일 좌표 체크하기
def cantMove(nowNM, moveNM, chessMap):
  moveN = nowNM[0] - moveNM[0]
  moveM = nowNM[1] + moveNM[1]
  if 0 < moveN < len(chessMap) and 0 < moveM < len(chessMap[0]):
    return False
  else:
    print('You can`t move there')
    return True


# sickKnight 내장함수 : 체스판 출력하기
def printMap(chessMap, nowNM):
  for line in chessMap:
    print(*line)
  print('Knight is (', nowNM[0], ',', nowNM[1], ') now.')
  print()


# 1. n >= 3 , m >= 7  --> 4번까지 이동 가능
# 2.
def sickKnight2():
  endN, endM = map(int, input().split())
  count = 0
  nowN, nowM = 0

  if endN >= 3 and endM >= 7:
    count = endM - 2

  elif endN == 2:
    if endM <= 2: count = 0
    elif endM <= 4: count = 1
    else: count = 2

  elif endN >= 3:
    if endM <= 0: count = 0


# 포기하고 답지 찾아봄
def sickKnight_ans():
  n, m = map(int, input().split())
  if n == 1:
    count = 1
  elif n == 2:
    count = min(4, (m - 1) // 2 + 1)
  elif m < 7:
    count = min(4, m)
  else:
    count = (2 + (m - 5)) + 1
  print(count)
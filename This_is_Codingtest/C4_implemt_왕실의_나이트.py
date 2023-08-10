""" 실전 문제 2 왕실의 나이트 """
# page 115

# 왕실 정원 체스판 8*8
# 행 : 1~8(세로좌표), 열 : a~h(가로좌표)
# 특정 칸에 나이트 하나 서있음
# 나이트 이동 규칙 : 수직2칸+수평1칸 or 수평2칸+수직1칸

# 입력 : 나이트의 위치(좌표 ex: a3)
# 출력 : 나이트 이동할 수 있는 경우의 수(개수)

#
""" my code """


def knightOfPalace():
  knight = input()
  k_row = int(knight[1])

  cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
  for i, c in enumerate(cols):
    if knight[0] == c:
      k_col = i + 1
      break
  k_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, 2), (1, -2), (2, 1),
             (2, -1)]

  count = 0

  for i in range(8):
    if 0 < k_row + k_moves[i][0] <= 8 and 0 < k_col + k_moves[i][1] <= 8:
      count += 1

  print(count)

  #
  """ answer code """

  def knightOfPalace_ans():
    # 현재 나이트 위치 입력 받기
    input_data = input()
    row = int(input_data[1])
    column = int(ord(input_data[0])) - int(ord('a')) + 1

    # 나이트 이동 방향 8개 정의
    steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1),
             (2, 1)]

    # 8가지 방향에 대해 각 위치로 이동 가능한지 확인
    result = 0
    for step in steps:
      # 이동하려는 위치 확인
      next_row = row + step[0]
      next_column = column + step[1]
      # 이동 가능하면 카운트 증가
      if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        result += 1

    print(result)

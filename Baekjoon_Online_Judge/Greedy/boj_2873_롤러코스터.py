""" 2873 : 롤러코스터 """

# 이 부지는 직사각형 모양이고, 상근이는 R행 C열의 표 모양으로 나누었다. 롤러코스터는 가장 왼쪽 위 칸에서 시작할 것이고, 가장 오른쪽 아래 칸에서 도착할 것이다. 롤러코스터는 현재 있는 칸과 위, 아래, 왼쪽, 오른쪽으로 인접한 칸으로 이동할 수 있다. 각 칸은 한 번 방문할 수 있고, 방문하지 않은 칸이 있어도 된다.

# 각 칸에는 그 칸을 지나갈 때, 탑승자가 얻을 수 있는 기쁨을 나타낸 숫자가 적혀있다. 롤러코스터를 탄 사람이 얻을 수 있는 기쁨은 지나간 칸의 기쁨의 합이다. 가장 큰 기쁨을 주는 롤러코스터는 어떻게 움직여야 하는지를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 R과 C가 주어진다. (2 ≤ R, C ≤ 1000) 둘째 줄부터 R개 줄에는 각 칸을 지나갈 때 얻을 수 있는 기쁨이 주어진다. 이 값은 1000보다 작은 양의 정수이다.

# 출력
# 첫째 줄에 가장 가장 큰 기쁨을 주는 롤러코스터는 가장 왼쪽 위 칸부터 가장 오른쪽 아래 칸으로 어떻게 움직이면 되는지를 출력한다. 위는 U, 오른쪽은 R, 왼쪽은 L, 아래는 D로 출력한다. 정답은 여러 가지 일 수도 있다.

#
""" my code """
# 힌트 : 짝 짝일 때는 행과 열의 합이 홀수인 지점 아무 곳이나 하나 고르는 것이 가능합니다.


def happyRolco():
  import sys
  inp = sys.stdin.readline
  r, c = map(int, inp().split())
  d = [list(map(int, inp().split())) for _ in range(r)]

  # LtoR = 1
  # UtoD = 1

  ans = ""

  # 둘 다 홀수일 때 + r만 홀수일 때 : RRR D LLL D 방향으로 돌기
  if r % 2 == 1:
    print(("R" * (c - 1) + "D" + "L" * (c - 1) + "D") * (r // 2) + "R" *
          (c - 1))
    #   원래 이렇게 짰었음
    # for i in range(r):
    #   if LtoR == 1: ans += 'R' * (c - 1) + 'D'
    #   else: ans += 'L' * (c - 1) + 'D'
    #   LtoR ^= 1

  # c만 홀수일 때 : DDD R UUU R 방향으로 돌기
  elif c % 2 == 1:
    print(("D" * (r - 1) + "R" + "U" * (r - 1) + "R") * (c // 2) + "D" *
          (r - 1))

    # for i in range(c):
    #   if UtoD == 1: ans += 'D' * (r - 1) + 'R'
    #   else: ans += 'U' * (r - 1) + 'R'
    #   UtoD ^= 1

  # 둘 다 짝수일 때 : r+c가 홀수인 제일 작은 칸 하나 버리고 다 돌기
  else:
    # 버릴 가장 작은 값 찾기
    minHapp = 1000
    for i in range(r):
      for j in range(c):
        if (i + j) % 2 == 1 and minHapp > d[i][j]:
          minHapp = d[i][j]
          minR = i
          minC = j

    # 막힌 r 찾고 막힌 r 피해서 돌아가기
    RDLD = 1  # RDLD=0 --> LDRD

    for k in range(r // 2):
      if k * 2 == minR or k * 2 + 1 == minR:
        if minC == 0:  # min 위치 [홀수][0]일 때
          ans += 'RD' + 'RURD' * ((c - 2) // 2) + 'D'

        elif minC == c - 1:  # min 위치 [짝수][c-1]일 때
          ans += 'DR' + 'URDR' * ((c - 2) // 2) + 'D'

        else:  # min 위치 [x][중간]일 때
          if minC % 2 == 1:  # min 위치 [x][홀수]일 때
            ans += 'DR' + 'URDR' * (minC // 2)
            ans += 'RURD' * ((c - minC - 1) // 2) + 'D'

          else:  # min 위치 [x][짝수]일 때
            ans += 'DRUR' * (minC // 2)
            ans += 'RDRU' * ((c - minC) // 2 - 1) + 'RDD'

        RDLD = 0

      else:
        if RDLD == 1:
          ans += 'R' * (c - 1) + 'D' + 'L' * (c - 1) + 'D'
        else:
          ans += 'L' * (c - 1) + 'D' + 'R' * (c - 1) + 'D'

  # 출력 (마지막 원소 빼고)
  print(ans[0:-1])


#
""" another way : for 문 안돌고 문자열 곱하기 연산으로 해결하기 """


def happyRolco_ans():
  import sys

  x, y = map(int, sys.stdin.readline().rstrip().split())
  r_map = [
    list(map(int,
             sys.stdin.readline().rstrip().split())) for _ in range(x)
  ]

  if x % 2 == 1:
    print(("R" * (y - 1) + "D" + "L" * (y - 1) + "D") * (x // 2) + "R" *
          (y - 1))
    exit(0)

  if y % 2 == 1:
    print(("D" * (x - 1) + "R" + "U" * (x - 1) + "R") * (y // 2) + "D" *
          (x - 1))
    exit(0)

  min_x, min_y = 0, 1
  min_t = 1001
  result = ""
  for i in range(x):
    for j in range((i + 1) % 2, y, 2):
      if r_map[i][j] <= min_t:
        min_x = i
        min_y = j
        min_t = r_map[i][j]

  # 앞부분 채우기
  result += ("R" * (y - 1) + "D" + "L" * (y - 1) + "D") * (min_x // 2)
  result += ("DRUR") * (min_y // 2)

  if min_y % 2 == 1 and min_x % 2 == 0:
    result += "DR"
  else:
    result += "RD"

  # 뒷 부분 채우기
  result += ("RURD") * ((y - min_y - 1) // 2)
  result += ("D" + "L" * (y - 1) + "D" + "R" *
             (y - 1)) * ((x - min_x - 1) // 2)

  print(result)
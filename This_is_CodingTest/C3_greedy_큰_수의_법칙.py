""" 문제 3-2 : 큰 수의 법칙 """

# 이 문제의 큰 수의 법칙 : 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
# 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과해서 더해질 수 없음

# ex)
# 배열 : [ 2, 4, 5, 4, 6 ]
# M : 8
# K : 3
# 큰 수의 법칙 결과 : 6+6+6+5+6+6+6+5 = 46

# 입력
# 첫째 줄에 N, M, K
# 둘째 줄에 N개의 자연수

# 출력
# 큰 수의 법칙 결과

#
""" 내가 푼 코드 """


def bigNum():
  import sys

  n, m, k = map(int, input().split())
  d = list(map(int, sys.stdin.readline().split()))
  d.sort()

  k1 = k
  res = 0

  while m > 0:

    if k1 == 0:
      res += d[-2]
      k1 = k

    else:
      res += d[-1]
      k1 -= 1

    m -= 1

  print(res)
bigNum()


""" 내가 푼 코드 2 """


def bigNum2():
  import sys

  n, m, k = map(int, input().split())
  d = list(map(int, sys.stdin.readline().split()))
  d.sort()

  res = (d[-1] * k + d[-2]) * (m // (k + 1)) + d[-1] * (m % (k + 1))
  print(res)


""" 정답 예시 """


def bigNum_ans():
  n, m, k = map(int, input().split())
  d = list(map(int, input().split()))
  d.sort()
  first = d[n - 1]  # d[n-1] == d[-1]
  second = d[n - 2]  # d[n-2] == d[-2]

  # 가장 큰 수가 더해지는 횟수 계산
  count = (m // (k + 1)) * k
  count += m % (k + 1)

  res = 0
  res += count * first
  res += (m - count) * second

  print(res)

""" 9095 : 1, 2, 3 더하기 """
# 문제
# 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

# 1+1+1+1
# 1+1+2
# 1+2+1
# 2+1+1
# 2+2
# 1+3
# 3+1
# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.

# 출력
# 각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.

#
""" my code """

def plus123() :
  import sys
  from itertools import product
  t = int(sys.stdin.readline().rstrip())
  for i in range(t) :
    n = int(sys.stdin.readline().rstrip())
    count = 0
    for j in range(1, n+1) :
      for i in product([1, 2, 3] ,repeat=j) :
        if sum(i) == n : count += 1
    print(count)


def plus123_ans() :
  T = int(input())
  a = [int(input()) for _ in range(T)]
  c = [0]*(11)
  c[1] = 1
  c[2] = 2
  c[3] = 4
  for i in range(4, 11):
      c[i] = c[i-1] + c[i-2] + c[i-3]
  for b in a:
      print(c[b])
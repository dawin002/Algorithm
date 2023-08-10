""" 1744 : 수 묶기 """

# 길이가 N인 수열이 주어졌을 때, 그 수열의 합을 구하려고 한다. 하지만, 그냥 그 수열의 합을 모두 더해서 구하는 것이 아니라, 수열의 두 수를 묶으려고 한다. 어떤 수를 묶으려고 할 때, 위치에 상관없이 묶을 수 있다. 하지만, 같은 위치에 있는 수(자기 자신)를 묶는 것은 불가능하다. 그리고 어떤 수를 묶게 되면, 수열의 합을 구할 때 묶은 수는 서로 곱한 후에 더한다.

# 예를 들면, 어떤 수열이 {0, 1, 2, 4, 3, 5}일 때, 그냥 이 수열의 합을 구하면 0+1+2+4+3+5 = 15이다. 하지만, 2와 3을 묶고, 4와 5를 묶게 되면, 0+1+(2*3)+(4*5) = 27이 되어 최대가 된다.

# 수열의 모든 수는 단 한번만 묶거나, 아니면 묶지 않아야한다.

# 수열이 주어졌을 때, 수열의 각 수를 적절히 묶었을 때, 그 합이 최대가 되게 하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수열의 크기 N이 주어진다. N은 50보다 작은 자연수이다. 둘째 줄부터 N개의 줄에 수열의 각 수가 주어진다. 수열의 수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다.

# 출력
# 수를 합이 최대가 나오게 묶었을 때 합을 출력한다. 정답은 항상 231보다 작다.


#
""" my code """
# 힌트 : 양수, 1, 0, -1, 음수 구분하기


def tieNumber():
  import sys
  n = int(sys.stdin.readline().rstrip())
  nums = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
  # print(nums)
  nums.sort(reverse=True)
  # print(nums)

  ans = 0
  nums_p = []
  nums_m = []
  # nums_z = 0
  # nums_p1 = 0
  # nums_m1 = 0
  # left_m = 0

  for x in nums:
    if x > 1 : nums_p.append(x)
    # elif x < -1: nums_m.append(x)
    # elif x == 1: nums_p1 += 1
    elif x == 1 : ans += 1  # 1은 바로 더해줘도 상관없음
    else : nums_m.append(x)   # 0, -1 도 음수랑 처리하면 더 편함
    # elif x == -1: nums_m1 += 1
    # else: nums_z += 1

    nums_m.sort()

  # 양수들 처리
  if len(nums_p) % 2 == 1 : nums_p.append(1)
  for i in range(0, len(nums_p), 2) :
    ans += nums_p[i] * nums_p[i + 1]

  # 개선된 음수 처리 (음수, -1, 0)
  if len(nums_m) % 2 == 1 : nums_m.append(1)
  for i in range(0, len(nums_m), 2) :
    ans += nums_m[i] * nums_m[i + 1]

  # # 음수들 처리
  # if len(nums_m) % 2 == 1:
  #   left_m = nums_m[-1]
  #   for i in range(0, len(nums_m) - 1, 2):
  #     ans += nums_m[i] * nums_m[i + 1]
  # else:
  #   for i in range(0, len(nums_m), 2):
  #     ans += nums_m[i] * nums_m[i + 1]

  # # 음수들 홀수개일 때 하나 남은 음수 처리
  # if left_m != 0:
  #   if nums_m1 != 0:
  #     nums_m1 -= 1
  #     left_m = -left_m
  #   elif nums_z != 0:
  #     nums_z -= 1
  #     left_m = 0
  #   ans += left_m

  # # -1 처리
  # if nums_m1 != 0:
  #   if nums_m1 % 2 == 0:
  #     ans += nums_m1 // 2
  #   else:
  #     ans += (nums_m1 - 1) // 2
  #     if nums_z == 0:
  #       ans -= 1

  # # 1 처리
  # ans += nums_p1

  print(ans)


#
""" better code """


def tieNumber_ans1():
  import sys
  input = sys.stdin.readline

  N = int(input())
  positive = []  # 양수를 저장할 리스트
  negative = []  # 음수를 저장할 리스트
  max_sum = 0

  for _ in range(N):
    n = int(input())

    if n > 1:
      positive.append(n)
    elif n == 1:
      max_sum += 1  # 1, 양수의 규칙에 의해 1을 더한다.
    else:
      negative.append(n)

  positive.sort(reverse=True)  # 양수의 큰 수부터 정렬한다.
  negative.sort()  # 음수의 작은 수부터 정렬한다.

  # 양수 리스트 더해주기
  if len(positive) % 2 == 0:  # 양수가 짝수개 일경우 두개씩 곱해준다.
    for i in range(0, len(positive), 2):
      max_sum += positive[i] * positive[i + 1]
  else:
    for i in range(0, len(positive) - 1, 2):
      max_sum += positive[i] * positive[i + 1]
    max_sum += positive[len(positive) - 1]  # 마지막 수는 더해준다.

  # 음수 더해주기
  if len(negative) % 2 == 0:  # 음수가 짝수개 일경우 두개씩 곱해준다.
    for i in range(0, len(negative), 2):
      max_sum += negative[i] * negative[i + 1]
  else:
    for i in range(0, len(negative) - 1, 2):
      max_sum += negative[i] * negative[i + 1]
    max_sum += negative[len(negative) - 1]  # 마지막 수는 더해준다.

  print(max_sum)
import time
""" 문제 3-4 : 1이 될 때까지 """

#
""" 내 풀이 코드 """


def untilOne():
  n, k = map(int, input().split())
  start_time = time.time()
  count = 0
  while n > 1:
    if n % k == 0:
      n = n // k
      count += 1
    else:
      if n != n % k:
        left = n % k
      else:
        left = n % k - 1
      n -= left
      count += left
  end_time = time.time()
  print(count)
  print("time :", round(end_time - start_time, 10))

  # 보완해야 할 부분
  # while 문을 반복하는 내내 1 < n < k 인지 확인하는데 반복 조건을 n >= k 로 주고
  # 반복 탈출 후의 n값과 1의 차이를 count에 더해주는게 더 효율적임


#
""" 내 풀이 코드 """


def untilOne2():
  n, k = map(int, input().split())
  start_time = time.time()
  count = 0
  while n >= k:
    if n % k == 0:
      n = n // k
      count += 1
    else:
      left = n % k
      n -= left
      count += left
  count += n - 1
  end_time = time.time()
  print(count)
  print("time :", round(end_time - start_time, 10))


#
""" 교재 정답 코드 """


def untilOne_ans():
  n, k = map(int, input().split())
  start_time = time.time()
  res = 0

  while True:
    target = (n // k) * k
    res += n - target
    n = target

    if n < k:
      break

    res += 1
    n //= k

  res += n - 1
  end_time = time.time()

  print(res)
  print("time :", round(end_time - start_time, 10))

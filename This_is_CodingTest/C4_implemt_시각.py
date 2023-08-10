""" 예제 4-2 시각 """
# page 113

#
""" my code ( faster ) """


def threeInTime():
  hour = int(input())
  hours = [3, 13, 23]
  _3In60 = [x for x in range(60) if x % 10 == 3 or x // 10 == 3]
  _3InMin = len(_3In60)
  _3InSec = len(_3In60)
  count = 0
  for h in range(hour + 1):
    if h in hours:
      count += 60 * 60
    else:
      count += _3InMin * 60 + (60 - _3InMin) * _3InSec
  print(count)


""" answer """


def threeInTime_ans():
  h = int(input())
  count = 0
  for i in range(h + 1):
    for j in range(60):
      for k in range(60):
        if '3' in str(i) + str(j) + str(k):
          count += 1
  print(count)
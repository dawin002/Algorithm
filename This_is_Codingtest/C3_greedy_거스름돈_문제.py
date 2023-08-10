""" 문제 3-1 : 거스름돈 문제 """

# 나는 음식점 캐셔.
# 카운터에 거스름돈용 동전 500, 100, 50, 10 무한하게 존재
# 손님에게 줄 거스름돈 N원일 때, 거슬러 줘야 할 동전의 최소 개수?
# 단, N은 10의 배수

#
""" 내가 푼 코드 """


def guss():
  n = int(input())
  gus = [500, 100, 50, 10]
  count = 0

  for i in range(4):
    coin = n // gus[i]
    n -= coin * gus[i]
    count += coin

  print(count)


#
""" 정답 코드 """


def guss_answer():
  n = int(input())
  count = 0
  coin_types = [500, 100, 50, 10]

  for coin in coin_types:
    count += n // coin
    n %= coin

  print(count)


""" 그리디 알고리즘 쓸 수 있는 이유 """
# 큰 단위의 동전이 작은 단위 동전의 배수여서
# 작은 단위의 동전을 합쳤을 때 다른 조합이 나오지 않기 때문
# 만약 동전 단위끼리 배수의 관계가 아니라면 그리디 알고리즘 이용 불가.
# 다이나믹 프로그래밍 활용해야 해결 가능.

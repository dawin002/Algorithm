""" 2875 : 대회 or 인턴 """

# 백준대학교에서는 대회에 나갈 때 2명의 여학생과 1명의 남학생이 팀을 결성해서 나가는 것이 원칙이다.

# 백준대학교는 N명의 여학생과 M명의 남학생이 팀원을 찾고 있다. 대회에 참여하려는 학생들 중 K명은 반드시 인턴쉽 프로그램에 참여해야 한다. 인턴쉽에 참여하는 학생은 대회에 참여하지 못한다.

# 여학생의 수 N, 남학생의 수 M, 인턴쉽에 참여해야하는 인원 K가 주어질 때
# 만들 수 있는 최대의 팀 수를 구하면 된다.

#
""" my code """


def inturn():
  n, m, k = map(int, input().split())
  # n:2, m:1 배수
  maxTeam = min(n // 2, m)
  restN = n - maxTeam * 2
  restM = m - maxTeam
  restInturn = k - (restN + restM)
  if restInturn > 0:
    maxTeam -= round(restInturn / 3 + 0.5)
  print(maxTeam)


#
""" better code """


def inturn_ans():
  n, m, k = map(int, input().split())
  print(min((n + m - k) // 3, n // 2, m))
  # 진짜 희한한듯;;
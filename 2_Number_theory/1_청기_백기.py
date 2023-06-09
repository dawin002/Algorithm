""" 1. 청기 백기 """

# n개의 깃발, n명의 참가자
# 기본 세팅 : 청색, 뒷면 백색
# 1번 사람은 1의 배수 모두 뒤집기
# 2번 사람은 2의 배수 모두 뒤집기
# 백색 이 앞면인 깃발 몇개?

# 1 2 3 4 5 6 7 8 9
# x x x x x x x x x
# o o o o o o o o o
#   x o x o x o x o
#     x x o o o x x
#       o o o o o x
#         x o o o x
#           x o o x
#             x o x
#               x x
#                 o

# 1 2 3 4 5 6 7 8 9
# o x x o x x x x o

# --> 루트가 정수인 수가 백색임
# 루트가 정수인 수의 개수를 찾으면 정답
# 근데 그 개수는 주어진 n에 루트를 씌우면 나옴

n = int(input())
ans = int(n ** (1/2))
print(ans)

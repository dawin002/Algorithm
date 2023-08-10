""" 2903 : 중앙 이동 알고리즘 """

# n box p
# 0 1   4
# 1 4   9
# 2 16  25
# 3 64  81

""" my solutioin """


def mid_move():
    n = int(input())
    a = 2
    for i in range(n):
        a = a + a - 1
    print(a * a)


mid_move()

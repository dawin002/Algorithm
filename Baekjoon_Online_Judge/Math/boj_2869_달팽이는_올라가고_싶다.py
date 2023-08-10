""" 2869 : 달팽이는 올라가고 싶다 """


""" my solution """

def snail_want_up():
    a, b, v = map(int, input().split())
    pre_v = v - b
    ans = pre_v // (a - b) + 1
    if pre_v % (a-b) == 0:
        ans -= 1
    print(ans)
snail_want_up()
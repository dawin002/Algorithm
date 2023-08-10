""" 2720 : 세탁소 사장 동혁 """

# 잔돈 문제(초간단)
# 첫줄 : 테케
# 둘째줄부터 : 거스름돈
# 잔돈 종류 : 25, 10, 5, 1

""" my solution """

def coin_simple():
    arr = [25, 10, 5, 1]
    for _ in range(int(input())):
        n = int(input())
        res = ''
        for a in arr:
            res += str(n//a) + ' '
            n %= a
        print(res[:-1])

coin_simple()
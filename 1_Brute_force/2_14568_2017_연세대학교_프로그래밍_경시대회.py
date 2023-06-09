""" 14568 - 2017 연세대학교 프로그래밍 경시대회 """

def yeonse_2017():
    n = int(input())
    count = 0
    for th in range(1, n + 1):
        for yh in range(1, n + 1):
            for ng in range(1, n + 1):
                if th + yh + ng == n:
                    if ng >= yh + 2:
                        if th % 2 == 0:
                            count += 1
    print(count)
yeonse_2017()
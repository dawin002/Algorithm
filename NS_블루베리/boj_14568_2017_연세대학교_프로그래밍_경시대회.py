""" 14568 - 2017 연세대학교 프로그래밍 경시대회 """

# tk, yh, ng 세명 n개 사탕을 나눠가짐
# 남는 사탕 0
# ng == yh + 2
# tk, yh, ng >= 1
# tk % 2 == 0

# 세명 사탕 나누는 방법 경우의 수
# 1 <= n <= 100

""" my solution """

def candy_split():
    n = int(input())
    count = 0
    for tk in range(2, n, 2):
        for yh in range(1, n - tk):
            ng = n - tk - yh
            if ng < yh :
                break
            if ng >= yh + 2:
                count += 1
    print(count)

candy_split()

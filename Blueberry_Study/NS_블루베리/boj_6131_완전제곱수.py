""" 6131 - 완전제곱수 """

# a, b (1 <=  b <= a <= 500)
# 규칙 : a^2 = b^2 + n
# 규칙 만족하는 a, b 쌍의 수 구하기
# n 입력 (1 <= n <= 1000)

""" my solution """

# 내 연산 횟수 : 500 * 250

def perfect_num():
    n = int(input())
    count = 0
    for b in range(1, 500):
        for a in range(b, 500):
            if a**2 == b**2 + n:
                count += 1
    print(count)
perfect_num()


""" answer """

# 정답 연산 횟수 : 최대 500

def perfect_num_ans():
    n = int(input())
    count = 0
    for b in range(1, 500):
        a = (b**2 + n) ** 0.5
        if a < b:
            break
        if int(a) == a:
            count += 1
    print(count)
perfect_num_ans()
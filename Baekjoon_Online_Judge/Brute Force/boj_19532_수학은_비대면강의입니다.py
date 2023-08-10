""" 19532 : 수학은 비대면강의입니다 """

# 연립방정식 풀기
# 식1 / : ax + by = c
# 식2 \ : dx + ey = f
# 입력 : -999 <= a, b, c, d, e, f <= 999 정수
# 식을 만족하는 -999 <= x, y <= 999 찾기

""" my solution """


def math_is_online():
    a, b, c, d, e, f = map(int, input().split())
    math_range = range(-999, 1000)
    count = 0
    for x in math_range:
        for y in math_range:
            count += 1
            if a * x + b * y - c == d * x + e * y - f == 0:
                print(x, y, count)
                break


math_is_online()

""" ??? """

def math_is_online_what():
    a, b, c, d, e, f = map(int, input().split())
    x = (e * c - b * f) // (a * e - b * d)
    y = (a * f - c * d) // (a * e - b * d)
    print(x, y)

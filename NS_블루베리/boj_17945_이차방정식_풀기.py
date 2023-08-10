""" 17945번 - 통학의 신 """

# x^2 + 2Ax + B = 0
# 위 방정식의 근들을 모두 공백으로 분리해 오름차순으로 출력
# 중근일 경우 하나만 출력
# A, B 주어짐 (-1000 <= A, B <= 1000)

""" my solution """

def god_of_go_school():
    a, b = map(int, input().split())
    # (x ** 2) + (2 * a * x) + b == 0
    # x^2 = 2000x + 1000
    ans = set()
    i = 0
    while i <= 2500:
        if len(ans) == 2:
            break
        x1 = i
        if x1 ** 2 + 2 * a * x1 + b == 0:
            ans.add(x1)
        x2 = -i
        if x2 ** 2 + 2 * a * x2 + b == 0:
            ans.add(x2)
        i += 1

    print(*sorted(list(ans)))

god_of_go_school()



""" hint solution : 근의 공식 적용해서 풀었는데, 이렇게 안푸는게 정답인듯 """

def god_of_go_school_h():
    a, b = map(int, input().split())
    # (x ** 2) + (2 * a * x) + b == 0
    # (x ** 2) + (2 * a * x) == -b
    # (x ** 2) + (2 * a * x) + (a ** 2) == -b + (a ** 2)
    # (x + a) ** 2 == a ** 2 - b
    # x + a = loot(a ** 2 - b)
    x1 = int((a ** 2 - b) ** 0.5 - a)
    x2 = int(-(a ** 2 - b) ** 0.5 - a)
    if x1 == x2:
        print(x1)
    else:
        print(min(x1, x2), max(x1, x2))


# god_of_go_school_h()

"""
    이차방정식 풀기 : 근의 공식
    
    a(x^2) + b(x) + c = 0
    
    x1 = (-b + loot(b^2 + 4ac)) / 2a
    x2 = (-b - loot(b^2 + 4ac)) / 2a
"""

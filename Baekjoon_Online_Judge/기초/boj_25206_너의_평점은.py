""" 25206 : 너의 평점은 """
# 학점 평균 계산
# A+ : 4.5
# A : 4.0
# ...
# D = 1.0
# F = 0.0
# P = NaN

""" my solution """


def your_grade():
    grade = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
    score = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]
    num_class = 0
    sum_class = 0
    for _ in range(20):
        cla, n, g = input().split()
        n = float(n)
        if g == 'P':
            continue
        sum_class += n * score[grade.index(g)]
        num_class += n
    print(sum_class / num_class)


your_grade()

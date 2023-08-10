""" 정렬 문제 : 23. 국영수 """

# 반 학생 N명 이름, 국어, 영어, 수학 점수 주어짐
# 다음 조건으로 성적 정렬하는 프로그램
# 1. 국어 점수 감소하는 순으로
# 2. 국어 점수 같으면 영어 점수 증가하는 순으로
# 3. 영어 점수까지 같으면 수학 점수 감소하는 순으로
# 4. 모든 점수 같으면 이름이 사전 순으로 증가하는 순으로
#
# 출력은 이름만 한줄에 한명씩

""" my solution """
# 정렬할 때 우선순위 낮은 key 부터 먼저 정렬한 후 우선순위 높은 key로 정렬하면 됨

def kor_eng_math():
    n = int(input())
    grades = []
    for _ in range(n):
        name, *grade = input().split()
        kor, eng, mat = map(int, grade)
        grades.append((name, kor, eng, mat))

    grades.sort(key=lambda x: x[0])
    grades.sort(reverse=True, key=lambda x: x[3])
    grades.sort(key=lambda x: x[2])
    grades.sort(reverse=True, key=lambda x: x[1])

    names = [grade[0] for grade in grades]
    print('\n'.join(names))

# kor_eng_math()



""" answer solution """

# 람다 함수를 더 잘 써보자
# students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]) )
# 위 코드 의미 :
#   1. x[1] 기준으로 내림차순 정렬
#   2. x[1] 같은 경우, x[2] 기준으로 오름차순 정렬
#   3. x[2] 같은 경우, x[3] 기준으로 내림차순 정렬
#   4. x[3] 같은 경우, x[0] 기준으로 오름차순 정렬

def kor_eng_math_ans():
    n = int(input())
    students = []
    for _ in range(n):
        name, *grades = input().split()
        grades = list(map(int, grades))
        students.append((name, *grades))

    students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

    names = [student[0] for student in students]

    print('\n'.join(names))

# kor_eng_math_ans()

def kor_eng_math_boj():
    import sys
    n = int(input())
    students = [(sys.stdin.readline().split()) for _ in range(n)]
    students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
    print('\n'.join([student[0] for student in students]))

# kor_eng_math_boj()
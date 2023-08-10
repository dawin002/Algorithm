""" 4779 : 칸토어 집합 """

# 칸토어 집합 : 0 과 1 사이의 실수로 이루어진 집합
# 각 구간을 3등분해 가운데 구간을 선택적으로 제외하는 방식
# '-'가 3^n개 있는 문자열
# 문자열 3등분 -> 가운데 문자열 ' '로 채우기 -> 모든 '-'선의 길이가 1이 될때까지

import sys

def canto(s):
    if len(s) == 1:
        return s
    ls = len(s) // 3
    s1 = canto('-' * ls)
    s2 = ' ' * ls
    return s1 + s2 + s1

lines = sys.stdin.readlines()

for line in lines:
    n = int(line)
    s = '-' * 3 ** n
    s = canto(s)

    print(s)

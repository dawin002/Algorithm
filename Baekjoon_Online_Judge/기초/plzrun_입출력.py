""" 1000 : A+B """
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
#
# """ my code """
def ab1():
    a, b = map(int, input().split())
    print(a + b)

# """ better code """
def ab1_ans():
    print( sum( map(int, input().split() ) ) )



""" 2558 : A+B - 2 """
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 A, 둘째 줄에 B가 주어진다. (0 < A, B < 10)

# """ my code """
def ab2():
    a = int(input())
    b = int(input())
    print(a+b)

# """ another way """
def ab2_ans():
    print( int(input()) + int(input()) )



""" 10950 : A+B - 3 """

# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 둘째 줄부터 T회 입력되는 두 정수 A와 B를 더해서 출력하는 프로그램을 작성하시오.
#
# """ my code (48ms) """
def ab3():
    for i in range(int(input())) :
    print(sum(map(int, input().split())))

# """ faster code (32ms) """
def ab3_fast():
    import sys
    t = int(input())
    for i in range(t):
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)

# """ faster code2 (32ms) """
def ab3_f2():
    import sys
    input()
    for i in sys.stdin:
        c = sum(map(int, i.split()))
        print(c)

# """ faster code3 (32ms) """
def ab3_f3():
    import sys
    read = sys.stdin.readline
    for _ in range(int(read().strip())):
        print(sum(list(map(int, read().split()))))

# """ my code2 : sys.stdin.readline() 활용"""
def ab3_another():
    import sys
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        s = sum(map(int, sys.stdin.readline().split()))
        print(s)



""" 10951 : A+B - 4 """

# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력은 여러 개의 테스트 케이스로 이루어져 있다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다.

# """ my code """
def ab4():
    import sys
    for r in sys.stdin :
        c = sum(map(int, r.split()))
        print(c)

# """ another way : using readlines() """
def ab4_f():
    import sys
    for line in sys.stdin.readlines():
        c = sum(map(int, line.split()))
        print(c)

# """ another way2 : more simple readlines() """
def ab4_f2():
    import sys
    lines = sys.stdin.readlines()
    for line in lines:
        print(sum(map(int, line.split())))



""" 10952 : A+B - 5 """

# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 입력은 여러 개의 테스트 케이스로 이루어져 있다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 입력의 마지막에는 0 두 개가 들어온다.
#
# """ my code (40ms) """
def ab5():
    import sys
    while True:
        a, b = map(int, sys.stdin.readline().split())
        if (a == 0 and b == 0) : break
        else : print(a+b)

# """ better code (40ms) """
# 반복탈출 조건식만 다름
#   if a == b == 0: break

# """ better code2 (44ms) """
# 문제의 조건이 0 < a,b < 10 이어서 sum(a,b)는 무조건 0 이상
def ab5_b():
    import sys
    for line in sys.stdin:
        c = sum(map(int, line.split()))
        if c > 0 : print(c)
        else : break

# """ 틀린 코드 (runtime error) """
# 1. readlines() 사용
# lines = sys.stdin.readlines().split()
# for line in lines :
#   a, b = map(int, line.split())

# 2. sum 사용
# print(sum(a, b))



""" 10953 : A+B - 6 """

# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. A와 B는 콤마(,)로 구분되어 있다. (0 < A, B < 10)

# """ my code (40ms) """
def ab6():
    import sys
    t = int(sys.stdin.readline().strip())
    for _ in range(t) :
        c = sum(map(int, sys.stdin.readline().split(',')))
        print(c)

# """ better code (40ms) """
def ab6_b():
    import sys
    t = int(input())
    for _ in range(t) :
        a, b = map(int, sys.stdin.readline().split(','))
        print(a + b)



""" 11021 : A+B - 7 """

# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 각 테스트 케이스마다 "Case #x: "를 d출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.

# """ 참고 문법 : f-string """
# age = 12
# print( f"안녕하세요 제 나이는 {age}살 입니다." )
# age += 1

# """ mycode """
def ab7():
    import sys
    t = int(input())
    for i in range(1, t+1):
        a, b = map(int, sys.stdin.readline().split())
        print(f"Case #{i}: {a+b}")

# """ another code """
# 출력문 형식 이렇게도 가능
# print("Case #",i+1,": ",a+b,sep='')



""" 11022 : A+B - 8 """
# 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다.
# x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.

# """ my code """
def ab8():
    import sys
    t = int(input())
    for i in range(1, t+1):
        a, b = map(int, sys.stdin.readline().split())
        print(f'Case #{i}: {a} + {b} = {a+b}')



""" 11718 : 그대로 출력하기 """
# 입력 받은 대로 출력하는 프로그램을 작성하시오.

# """ my code """
def just_print():
    import sys
    for _ in range(100):
        print(sys.stdin.readline().strip())

# """ better code """
def just_print_b():
    import sys
    for line in sys.stdin:
        print(line, end="") # end="" 하는 이유는 stdin 으로 불러오는 입력 객체는 \n문자까지 포함되어 있기 때문에

# """ another way : open(0) ??? """
def just_print_o():
    print(open(0).read())



""" 11719 : 그대로 출력하기 2"""
# 입력받은 그대로 출력한다.
#     Hello
#
# Baekjoon
#    Online Judge

# """ my code """
def just_print2():
    import sys
    for line in sys.stdin :
        print(line, end='')

# """ better code """
def just_print2_b():
    import sys
    print(sys.stdin.read())



""" 11720 : 숫자의 합 """
# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.
# 첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.

# """ my code """
def sum_num():
    n = int(input())
    a = input()
    sum = 0
    for i in range(n):
      sum += int(a[i])
    print(sum)

# """ best code """
def sum_num2():
    n = int(input())
    print(sum([int(a) for a in input()]))

# """ another way """
def sum_num2_a():
    n = int(input())
    l = list(input())
    sum = 0
    for a in l :
      sum += int(a)
    print(sum)



""" 11721 : 열 개씩 끊어 출력하기 """
# 알파벳 소문자와 대문자로만 이루어진 단어가 주어진다.
# 이 단어를 한 줄에 10글자씩 끊어서 출력하는 프로그램을 작성하시오.

# """ my code """
def slice_ten():
    a = input()
    len = len(a)
    for i in range(len//10) :
        print(a[i*10:i*10+10])
    if len%10 != 0 :
        print(a[len//10*10:len])

# """ best code : while """
def slice_ten_while():
    line = input()
    i = 0
    while i < len(line):
        print(line[i:i+10])
        i += 10

# """ best code 2 : for """
def slice_ten_for():
    n = input()
    for i in range(0, len(n), 10):
      print(n[i : i + 10])



""" 2741 : N 찍기 """
# 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

# """ my better code (88ms) """
def print_n():
    n = int(input())
    l = [k for k in range(1, n+1, 1)]
    print(*l, sep='\n')

# """ my wrong code : 출력 초과 """
def print_n_w():
    n = int(input())
    i=1
    while i <= n+1 :
      print(i)

# """ best code (60ms) """
def print_n_b():
    n = int(input())
    print("\n".join(map(str, range(1, n + 1))))

#
""" 참고 문법 : *list """
# list 앞에 '*'을 붙여 *list 를 쓰면 리스트가 분해되어 반환된다
# 예시
# l = [1, 2, 3]
# print(l)    --> [1, 2, 3]
# print(*l)   --> 1, 2, 3



""" 2742 : 기찍 N """
# 자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

# """ my code (== best code) """
def print_n_reverse():
    print('\n'.join(map(str, range(int(input()), 0, -1))))

""" 참고 파이썬 문법 : '구분자'.join() """
# join 함수는 매개변수로 받는 리스트를 하나의 문자열로 합쳐주는 함수이다.
# '구분자'에 넣는 문자를 구분자로 리스트의 원소들을 연결시킨다.
# 예시
# li = ['a', 'b', 'c']
# '_'.join(li)    --> "a_b_c"
# ''.join(li)     --> "abc"
# '.\t'.join(li)  --> "a.  b.  c"



""" 2739 : 구구단 """
# N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

# """ my code """
def print_99():
    n = int(input())
    for i in range(1, 10):
        print(f"{n} * {i} = {n*i}")


# """ another way """
def print_99_a():
    n = int(input())
    for i in range(1, 10):
        print(n ,'*', i, '=', n*i)



""" 2007년 """
# 오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까? 이를 알아내는 프로그램을 작성하시오.
# 첫째 줄에 빈 칸을 사이에 두고 x(1 ≤ x ≤ 12)와 y(1 ≤ y ≤ 31)이 주어진다. 참고로 2007년에는 1, 3, 5, 7, 8, 10, 12월은 31일까지, 4, 6, 9, 11월은 30일까지, 2월은 28일까지 있다.
# 첫째 줄에 x월 y일이 무슨 요일인지에 따라 SUN, MON, TUE, WED, THU, FRI, SAT중 하나를 출력한다.

# """ my code """
def year_2007():
    m, d = map(int, input().split())
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    for i in range(m-1) :
        d += month[i]
    print(week[d%7])


# """ best code : 최고 간결성 코드 """
def year_2007_b():
    days = [0,31,28,31,30,31,30,31,31,30,31,30]
    m, d = map(int,input().split())
    week = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    print(week[(sum(days[:m])+d)%7])



""" 8393 : 합 """
# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

# """ my code (44ms) """
def sum_():
    n = int(input())
    d = [ i for i in range(n+1) ]
    print(sum(d))


# """ my faster code (40ms) """
def sum_f():
    n = int(input())
    sum = 0
    for i in range(n+1):
      sum += i
    print(sum)



""" 10818 : 최소, 최대 """

# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
# 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다.
# 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다.
# 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

# """ my code (416) """
def min_max():
    n = int(input())
    d = list(map(int, input().split()))
    min = max = d[0]
    for i in d :
        if min > i :
            min = i
        if max < i :
            max = i
    print(min, max)

# """ my wrong code"""
# min = 1000000
# max = 0

# """ my faster code (372)"""
def min_max_my_f():
    n = int(input())
    d = list(map(int, input().split()))
    print(min(d), max(d))

# """ another code1 (컴프리헨션 + input() ) : slowest(480) """
def min_max_slow():
    n = int(input())
    d = [int(a) for a in input().split()]
    print(min(d), max(d))

# """ another code2 (컴프리헨션 + read() ) : fastest(332) """
def min_max_f():
    import sys
    input()
    d = [int(a) for a in sys.stdin.read().split()]
    print(min(d), max(d))

# """ another code3 (컴프리헨션 + readline() ) : faster(388) """
def min_max_f2():
    import sys
    input()
    d = [int(a) for a in sys.stdin.readline().split()]
    print(min(d), max(d))



""" 2438 : 별 찍기 - 1 """
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제


# """ my code """
def print_star_1():
    n = int(input())
    for i in range(1, n+1):
        print('*' * i)


# """ better code """
def print_star_1_b():
    for i in range(int(input())) :
        print((i+1)*'*')



""" 2439 : 별 찍기 - 2 """
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
# 하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

# """ my code (44ms) """
def print_star_2():
    n = int(input())
    for i in range(n):
        print((n-i-1)*' ', end='')
        print((i+1)*'*')

# """ better code (40ms) """
def print_star_2_b():
    n=int(input())
    [print(' '*(n-i)+'*'*i) for i in range(1,n+1)]



""" 2440 : 별 찍기 - 3 """
# 첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제

# """ my code """
def print_star_3():
    [print('*'*(i)) for i in range(int(input()), 0, -1)]



""" 2441 : 별 찍기 - 4 """
# 첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제
# 하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

# """ my code"""
def print_star_3():
    n = int(input())
    [print(' '*i, '*'*(n-i), sep='') for i in range(n)]



""" 2442 : 별 찍기 - 5 """
# 첫째 줄에는 별 1개, 둘째 줄에는 별 3개, ..., N번째 줄에는 별 2×N-1개를 찍는 문제
# 별은 가운데를 기준으로 대칭이어야 한다.

# """ my code (비효율적) """
def print_star_5():
    n = int(input())
    [print(' '*((n-(2*i+1)//2-1)) + '*'*(2*i+1)) for i in range(n)]

# """ better code """
def print_star_5_b():
    n = int(input())
    [print((n-i)*" "+"*"*(2*i-1)) for i in range(1,n+1)]



""" 2445 : 별 찍기 - 8 """
# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.
# 예제 입력
# 5
# 예제 출력
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *

# """ my code """
def print_star_8():
    n = int(input())
    for i in range(1, n) :
        print('*'*i + ' '*(2*(n-i)) + '*'*i)
    for i in range(n, 0, -1):
        print('*'*i + ' '*(2*(n-i)) + '*'*i)



""" 2522 : 별 찍기 - 12 """
# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
# 예제 입력
# 3
# 예제 출력
#   *
#  **
# ***
#  **
#   *


# """ my code (52ms) """
def print_star_12():
    n = int(input())
    for i in range(1, n):
        print(' '*(n-i) + '*'*i)
    for i in range(n, 0, -1):
        print(' '*(n-i) + '*'*i)

# """ my code 2 (40ms faster) : 리스트 컴프리헨션 """
def print_star_12_my_f():
    n = int(input())
    [print(' '*(n-i) + '*'*i) for i in range(1, n)]
    [print(' '*(n-i) + '*'*i) for i in range(n, 0, -1)]


# """ best code : abs (절대값 이용) """
def print_star_12_b():
    n = int(input())
    for i in range(1,n*2):
        print(" "*abs(n-i) + "*"*(n-abs(n-i)) )



""" 2446 : 별 찍기 - 9 """
# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

# 예제 입력
# 5

# 예제 출력
# *********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********


# """ my code """
def print_star_9():
    n = int(input())
    for i in range(1, n*2):
        print( ' '*(n-abs(n-i)-1)  + '*'*(abs(n-i)*2+1))

# r   n  i    x
# 10  5  1    1
# 10  5  2    2
# 10  5  3    3
# 10  5  4    4
# 10  5  5    5
# 10  5  6    4
# 10  5  7    3
# 10  5  8    2
# 10  5  9    1


# """ another way """
def print_star_9_a():
    N=int(input())
    for i in range(1,2*N) :
        print(' '*(min(i,2*N-i)-1)+'*'*(1+2*(N-min(2*N-i,i))))



""" 10991 : 별 찍기 - 16 """
# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

# 예제 입력
# 4

# 예제 출력
#    *
#   * *
#  * * *
# * * * *

# """ my code """
def print_star_16():
    n = int(input())
    for i in range(1, n+1):
        print(' '*(n-i), end='')
        print('* '*i)



""" 10992 : 별 찍기 - 17 """
# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

# 예제 입력
# 4

# 예제 출력
#    *
#   * *
#  *   *
# *******


# """ my code """
def print_star_17():
    n = int(input())
    if n!=1 :
        print(' '*(n-1) + '*')
        for i in range(2, n):
            print(' '*(n-i), end='')
            print('*'+' '*((i-1)*2-1)+'*')
        print('*'*(n*2-1))
    else :
        print('*')


# """ best code """
def print_star_17_b():
    n = int(input())
    for i in range(n - 1):
        print(' ' * (n - i - 1) + '*' + ' ' * (2 * i - 1) + '*' * (i and 1))
    print('*' * (2 * n - 1))

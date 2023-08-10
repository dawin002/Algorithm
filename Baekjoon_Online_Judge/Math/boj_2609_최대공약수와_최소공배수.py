""" 2609 : 최대공약수와 최소공배수 """

# 문제
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

# 출력
# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

#
""" my code """


def GCDnLCM():
    a, b = map(int, input().split())

    if a < b:
        a, b = swap(a, b)

    gcdd = gcd(a, b)
    lcmm = lcm(a, b, gcdd)

    print(gcdd, lcmm, sep='\n')


def swap(a, b):
    tmp = b
    b = a
    a = tmp
    return a, b


# 최대공약수
def gcd(a, b):
    while b > 0:
        t = b
        b = a % b
        a = t
    return a


# 최대공약수 짧은 코드
def gcd2(a, b):
    while b > 0:
        a, b = b, a % b
    return a


# 최소공배수
def lcm(a, b, gcd_):
    return a * b // gcd_


#
""" shorter code """


def GCDnLCM_s():
    a, b = map(int, input().split())
    s = a * b
    while a % b != 0:
        a, b = b, a % b
    print(b)
    print(s // b)

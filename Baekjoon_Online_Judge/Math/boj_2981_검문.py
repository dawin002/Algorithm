""" 2981 : 검문 """

# 문제
# 검문받는 동안 할일 없어서 수학 게임 하는 중.
# 먼저 근처에 보이는 숫자 N개를 종이에 적는다.
# 그 다음, 종이에 적은 수를 M으로 나누었을 때, 나머지가 모두 같게 되는 M을 모두 찾으려고 한다.
# M은 1보다 커야 한다.
# N개의 수가 주어졌을 때, 가능한 M을 모두 찾는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 종이에 적은 수의 개수 N이 주어진다. (2 ≤ N ≤ 100)
# 다음 줄부터 N개 줄에는 종이에 적은 수가 하나씩 주어진다.
# 이 수는 모두 1보다 크거나 같고, 1,000,000,000보다 작거나 같은 자연수이다.
# 같은 수가 두 번 이상 주어지지 않는다.
# 항상 M이 하나 이상 존재하는 경우만 입력으로 주어진다.

# 출력
# 첫째 줄에 가능한 M을 공백으로 구분하여 모두 출력한다. 이때, M은 증가하는 순서이어야 한다.

#
""" 참고 힌트 ( 이거 없으면 못품 )"""

""" 참조 : https://velog.io/@ledcost/백준-2981-파이썬-검문-골드5-정수론 """


# 수학적 지식이 필요하다.
# A = M * a + R
# B = M * b + R
# C = M * c + R

# 이렇게 둬보자.(문제 조건에 부합하는 식, M으로 각 수를 나눴을 때 나머지가 모두 같다)
# B - A = M(b-a)
# C- B = M(c-b)

# 이런 원리로, A~Z까지 입력받은 모든 수에 대해(오름차순), M은 B - A, C -B, ..., Z - Y의 공약수들이다.
# 즉, 이웃한 것끼리 뺀 수들의 최대공약수의, 1을 제외한 모든 약수가 M이 될 수 있는 것이다.


# 최대공약수
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


""" my code """


def whileChecking():
    import sys
    N = int(sys.stdin.readline().rstrip())
    arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

    arr.sort(reverse=True)

    n_arr = [arr[i] - arr[i + 1] for i in range(N - 1)]

    M = n_arr[0]

    for i in range(1, N - 1):
        M = gcd(M, n_arr[i])

    # 약수 구하는 방식 잘못됨
    # for i in range(2, int(M**0.5)+1) :
    #   if M%i == 0 :
    #     print(i)

    result = set()
    for i in range(2, int(M ** 0.5) + 1):
        if M % i == 0:
            result.add(i)
            result.add(M // i)
    result.add(M)
    print(*sorted(list(result)))
""" 9020 : 골드바흐의 추측 """

# 문제
# 1보다 큰 자연수 중에서  1과 자기 자신을 제외한 약수가 없는 자연수를 소수라고 한다.
# 예를 들어, 5는 1과 5를 제외한 약수가 없기 때문에 소수이다.
# 하지만, 6은 6 = 2 × 3 이기 때문에 소수가 아니다.

# 골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다.
# 이러한 수를 골드바흐 수라고 한다. 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다.
# 예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다.
# 10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.

# 2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오.
# 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고 짝수 n이 주어진다.

# 출력
# 각 테스트 케이스에 대해서 주어진 n의 골드바흐 파티션을 출력한다. 출력하는 소수는 작은 것부터 먼저 출력하며, 공백으로 구분한다.

#
""" my code """


# 1. 5000 이하 소수 모두 구할 것
# 2. 입력받은 n 의 골드바흐 파티션 찾아서 출력할 것


def goldbagh():
    import sys

    pnl = [True] * 10001
    pnl[0] = False
    pnl[1] = False

    for i in range(2, len(pnl)):
        if pnl[i]:
            j = 2
            while i * j < len(pnl) - 1:
                pnl[i * j] = False
                j += 1

    T = int(sys.stdin.readline().rstrip())

    for _ in range(T):
        n = int(sys.stdin.readline().rstrip())

        parA = 0
        parB = 0
        parD = 10000
        for i in range(2, int(n / 2) + 1):
            if pnl[i] and pnl[n - i]:
                if parD > abs(i - (n - i)):
                    parD = abs(i - (n - i))
                    parA = i
                    parB = n - i

        print(parA, parB)


#
""" better code """


def goldbagh_ans():
    import sys

    sieve = [False, False, True] + [True, False] * 4999
    for i in range(3, int(10000 ** .5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * len(sieve[i * i::2 * i])

    num = int(sys.stdin.readline().strip())
    for i in range(num):
        number = int(sys.stdin.readline().strip())

        # 4는 못잡아서 예외처리
        if number == 4:
            print("2 2")
            continue

        # 여기가 핵심 코드
        # : n의 반부터 시작해서 더 빨리 끝나게
        start = number // 2

        if start % 2 == 0:
            start -= 1

        for j in range(start, 0, -2):
            if sieve[j] and sieve[number - j]:
                print(j, number - j)
                break

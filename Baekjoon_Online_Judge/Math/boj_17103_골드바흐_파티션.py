""" 17103 : 골드바흐 파티션 """

# 문제
# 골드바흐의 추측: 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.
# 짝수 N을 두 소수의 합으로 나타내는 표현을 골드바흐 파티션이라고 한다. 짝수 N이 주어졌을 때, 골드바흐 파티션의 개수를 구해보자.
# 두 소수의 순서만 다른 것은 같은 파티션이다.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T (1 ≤ T ≤ 100)가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 N은 짝수이고, 2 < N ≤ 1,000,000을 만족한다.

# 출력
# 각각의 테스트 케이스마다 골드바흐 파티션의 수를 출력한다.

#
""" my code """

def goldbagh3() :

    import sys
    input = sys.stdin.readline

    T = int(input().rstrip())
    lstN = []
    for _ in range(T) :
        lstN.append(int(input().rstrip()))
    maxG = max(lstN)
    prime = [2]
    prime_set = {2}

    # make goldbagh
    gold = [False, False, True] + [True, False]*( maxG // 2 - 1)
    for i in range(3, maxG+1, 2) :
        if gold[i] :
            prime.append(i)
            prime_set.add(i)
            for j in range(3, maxG+1, 2):
                if i * j > maxG :
                    break
                gold[i*j] = False


    for a in lstN :
        count = 0
        idx = 0
        while prime[idx] * 2 <= a :
            if a - prime[idx] in prime_set :
                count += 1
            idx += 1
        print(count)

goldbagh3()

""" better code """

def goldbagh3_b():
    maxG = 1000000
    gold = [0, 0] + [1] * (maxG - 1)

    for i in range(2, int(maxG ** .5 + 1.5)):
        if gold[i] :
            gold[i * 2::i] = [0] * (maxG // i - 1)

    lst_prime = [ x for x in range(maxG + 1) if gold[x] ]
    set_prime = { x for x in range(maxG + 1) if gold[x] }

    def check(n):
        cnt = 0
        for i in lst_prime:
            if i > n // 2: break
            cnt += n - i in set_prime
        return cnt

    N = int(input())
    while N :
        N -= 1
        print(check(int(input())))

goldbagh3_b()



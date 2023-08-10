""" 4948 : 베르트랑 공준 """

# 문제
# 베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.

# 자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오.

# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 케이스는 n을 포함하는 한 줄로 이루어져 있다.

# 입력의 마지막에는 0이 주어진다.

# 출력
# 각 테스트 케이스에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력한다.

#
""" my code """


def bertrang():
    table = bert_prime(0, 123456 * 2)
    # for i in range(13, 13*2+1) :
    #   print(i, ',', table[i])

    while True:
        N = int(input())
        if N == 0: break
        count = 0
        for i in range(N + 1, N * 2 + 1):
            if table[i] == True:
                count += 1
        print(count)


def bert_prime(n, m):
    table = [True] * (m + 1)
    table[0] = False
    table[1] = False

    for a in range(2, m + 1):
        if table[a] == True:
            b = 2
            while (a * b) <= m:
                table[a * b] = False
                b += 1
    return table


#
""" my code 2 """


def bertrang2():
    m = 123456
    table = [True] * (2 * m + 1)
    table[0] = False
    table[1] = False

    for a in range(2, 2 * m + 1):
        if table[a] == True:
            b = 2
            while (a * b) <= 2 * m:
                table[a * b] = False
                b += 1

    while True:
        N = int(input())
        if N == 0: break
        count = 0
        for i in range(N + 1, N * 2 + 1):
            if table[i] == True:
                count += 1
        print(count)

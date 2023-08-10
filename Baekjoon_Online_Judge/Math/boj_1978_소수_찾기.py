""" 1978 : 소수 찾기 """

# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

# 출력
# 주어진 수들 중 소수의 개수를 출력한다.

#
""" my code """


def prime_number_2():
    input()
    arr = list(map(int, input().split()))

    count = 0
    for a in arr:
        if a == 1: continue
        for i in range(2, int(a ** 1 / 2) + 1):
            if a % i == 0:
                break
        else:
            count += 1

    print(count)


""" test1 : for-else 문 """


def test1():
    for a in range(5):
        for b in range(5):
            pass
        else:
            print('for b - else')

    else:
        print('for a - else')

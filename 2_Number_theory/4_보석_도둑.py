""" 4. 보석 도둑 """

# 무게 총합 k 만큼 훔치려함
# n개의 보석 무게 : n개 보석 각 무게의 곱
# 보석 무게 : 2 ~ 무제한, 개수 무한
# 그 때의 보석 개수 최대값
# 1 <= k <= 10^12

""" my solution """

# 생각해보면 k 소인수분해 문제

def steal():
    k = int(input())
    arr = []
    for i in range(2, int(k**0.5)+2):
        while k % i == 0:
            arr.append(i)
            k //= i
    if k > 1:
        arr.append(k)
    print(len(arr))
    print(*arr)


def steal_2():
    k = int(input())
    arr = []
    while True:
        for i in range(2, int(k**0.5)+1):
            if k % i == 0:
                arr.append(i)
                k //= i
                break
        else:
            break
    if k > 1:
        arr.append(k)
    print(len(arr))
    print(*arr)

# steal_2()


def steal_3():
    k = int(input())
    arr = []
    count = 0
    for i in range(2, int(k**0.5)+2):
        while k % i == 0:
            count += 1
            arr.append(i)
            k //= i
    if k > 1:
        arr.append(k)
        count += 1
    print(count)
    print(*arr)
steal_3()


def steal_4():
    n = int(input())
    i = 2
    count = 0
    answer = []
    while n != 1:
        if i >= 100000:
            answer.append(n)
            count += 1
            break
        if n % i == 0:
            n //= i
            count += 1
            answer.append(i)
        else:
            i += 1

    print(count)
    print(*answer)
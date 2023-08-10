""" 5. 실질적 약수 """

# A, B 주어질 때
# A = B * C 를 만족하는 C : A의 약수
# 실질적 약수 : N의 약수 중 1 과 N을 제외한 약수
# SOD(Sum Of Divisor) : 어떤 수의 실질적 약수의 합
# CSOD(Cumulative SOD) : SOD(1) + SOD(2) + ... + SOD(n)
# CSOD 구현해 CSOD(n) % 1백만 한 값 출력

""" my solution """

def sod_1(n):
    res = set()
    for i in range(2, int(n**0.5)+2):
        if n % i == 0:
            res.add(i)
            res.add(n//i)
    return sum(res)

def csod_1():
    n = int(input())
    # arr = [set([]) for _ in range(0, n+1)]
    ans = 0
    for i in range(4, n+1):
        ans += sod_1(i)
        # if not arr[i]:
        #     arr[i] = sod_1(i)
        #     j = 2
        #     while i*j <= n:
        #         if not arr[i*j]:
        #             arr[i*j] = arr[i]
        #         arr[i*j].add(i)
        #         arr[i*j].add(j)
        #         j += 1
        # if arr[i]:
        #     ans += sum(arr[i])

    # for i in range(n+1):
    #     arr[i] = list(set(arr[i]))

    # print(arr)
    print(ans)

# csod_1()


""" answer solution """

def csod_2():
    n = int(input())
    sum = 0
    i = 2
    while i <= n//2:
        k = n // i
        b = n // k
        c = (k-1) * (b-i+1) * (i+b) // 2
        sum = (sum + c) % 1_000_000
        i = b + 1
    print(sum)
csod_2()

# 1
# 2
# 3
# 4 2           -> 2
# 5
# 6 2 3         -> 5
# 7
# 8 2 4         -> 6
# 9 3           -> 3
# 10 2 5        -> 7
# 11
# 12 2 3 4 6    -> 9
# 13
# 14 2 7        -> 9
# 15 3 5        -> 8
# 16 2 4 8      -> 14
# 17
# 18 2 9        -> 11
# 19
# 20 2 4 5 10   -> 14
# 21 3 7
# 22 2 11
# 23
# 24 2 3 4 6 8 12
# 25
""" DP 문제 : 못생긴 수 """

# 2,3,5 만을 소인수로 가지는 수
# 2,3,5 만을 약수로 가지는 수
# 2,3,5 끼리는 섞여도 상관 없는 듯

""" my solution : 맞은 줄 알았는데 틀림 """
# 1000개의 못생긴 수열이 있는 것이지, 1000까지의 수에 대한 못생긴 수열을 만드는 게 아님
# 따라서 내가 짠 코드로는 n = 86일 때 까지밖에 못 구함 ( n = 8 --> ans = 1000 )

def ugly_num():
    n = int(input())
    dp = [False] * 1001
    dp[1] = True
    n_set = {2, 3, 5}
    for i in range(501):
        if dp[i]:
            for s in n_set:
                if i * s <= 1001:
                    dp[i * s] = True
    count = 0
    i = 0
    while True:
        if dp[i]:
            result = i
            count += 1
            if count >= n:
                break
        i += 1

    print(result)


ugly_num()


""" answer solution """

def ugly_num_ans():
    n = int(input())
    ugly = [0] * n
    ugly[0] = 1

    i2 = i3 = i5 = 0
    next2, next3, next5 = 2, 3, 5

    for j in range(1, n):
        ugly[j] = min(next2, next3, next5)

        if ugly[j] == next2:
            i2 += 1
            next2 = ugly[i2] * 2

        if ugly[j] == next3:
            i3 += 1
            next3 = ugly[i3] * 3

        if ugly[j] == next5:
            i5 += 1
            next5 = ugly[i5] * 5

    print(ugly[n-1])
    print(ugly[:])

ugly_num_ans()



# input1
# 10
# out : 12

# input2
# 4
# out : 4

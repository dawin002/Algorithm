""" 2839 : 설탕 배달 """

# n 만큼의 설탕 배달해야 함
# 설탕 봉지 단위 : 3, 5
# 정확히 n 맞출 봉지 최소값

""" my solution """


def sugar_delivery():
    n = int(input())
    sug_5 = n // 5
    ans = -1

    while sug_5 >= 0:
        sug_left = n - 5 * sug_5
        sug_3 = sug_left // 3
        if 5 * sug_5 + 3 * sug_3 == n:
            ans = sug_5 + sug_3
            break
        sug_5 -= 1

    print(ans)


""" better solution """


def sugar_delivery_b():
    n = int(input())
    ans = 0
    while n >= 0:
        if n % 5 == 0:
            ans += n // 5
            print(ans)
            break
        n -= 3
        ans += 1
    else:
        print(-1)

sugar_delivery_b()
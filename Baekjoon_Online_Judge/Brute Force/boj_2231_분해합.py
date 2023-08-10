""" 2231 : 분해합 """

# 분해합 : 245의 분해합 = 245 + 2 + 4 + 5 = 256
# 245: 생성자, 256: 분해합
# 주어진 수 N에 대한 생성자 중 최소값 구하라 (없으면 0)

""" my solution """

def div_sum():
    n = input()
    len_n = len(n)
    n = int(n)
    res = 0
    find_range = range( max(n - len_n * 9, 0), min(n - len_n * 1 + 1, n) )
    for i in find_range:
        if i + sum(map(int, list(str(i)))) == n:
            res = i
            # print(i, list(map(int, list(str(i)))), i + sum(map(int, list(str(i)))))
            break

    print(res)

div_sum()
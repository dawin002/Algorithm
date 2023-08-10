""" 구현 문제 : 13. 치킨 배달 """

""" my code """

def chicken_delivery():
    from itertools import combinations

    def get_city_distance(home_list, store_list):
        ct_dis = 0
        for home in home_list:
            hx, hy = home
            min_dis = 1001
            for store in store_list:
                sx, sy = store
                now_dis = abs(hx - sx) + abs(hy - sy)
                if now_dis <= min_dis:
                    min_dis = now_dis
            ct_dis += min_dis
        return ct_dis

    n, m = map(int, input().split())
    ct_map = []
    for _ in range(n):
        ct_map.append(list(map(int, input().split())))

    store_list = set()
    home_list = set()

    for i in range(n):
        for j in range(n):
            if ct_map[i][j] == 1:
                home_list.add((i, j))
            elif ct_map[i][j] == 2:
                store_list.add((i, j))

    min_ct_dis = int(1e9)
    for comb in combinations(store_list, m):
        print(comb)
        now_ct_dis = get_city_distance(home_list, comb)
        if now_ct_dis < min_ct_dis:
            min_ct_dis = now_ct_dis

    print(min_ct_dis)

chicken_delivery()



""" answer code """

def chicken_delivery_ans():
    from itertools import combinations

    n, m = map(int, input().split())
    chicken, house = [], []

    for r in range(n):
        data = list(map(int, input().split()))
        for c in range(n):
            if data[c] == 1:
                house.append((r, c))
            elif data[c] == 2:
                chicken.append((r, c))

    candidates = list(combinations(chicken, m))

    def get_sum(candidate):
        result = 0
        for hx, hy in house:
            temp = 1e9
            for cx, cy in candidate:
                temp = min(temp, abs(hx-cx) + abs(hy-cy))
            result += temp
        return result

    result = 1e9
    for candidate in candidates:
        result = min(result, get_sum(candidate))

    print(result)

# input
# 5 3
# 0 0 1 0 0
# 0 0 2 0 1
# 0 1 2 0 0
# 0 0 1 0 0
# 0 0 0 0 2

# input2
# 5 2
# 0 2 0 1 0
# 1 0 1 0 0
# 0 0 0 0 0
# 2 0 0 1 1
# 2 2 0 1 2

# input3
# 5 1
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0

# input4
# 5 1
# 1 2 0 2 1
# 1 2 0 2 1
# 1 2 0 2 1
# 1 2 0 2 1
# 1 2 0 2 1
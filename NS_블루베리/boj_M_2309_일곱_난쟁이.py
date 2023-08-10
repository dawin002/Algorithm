""" 2309번 - 일곱 난쟁이 """

# 9명의 난쟁이 중 진짜 7명 찾기
# 진짜의 키를 다 합치면 100cm
# 각 줄마다 난쟁이 키 입력
# 일곱 난쟁이 키 오름차순으로 출력
# 여러 답이 있으면 아무거나 출력

""" my solution """

def seven_small():
    arr = [int(input()) for _ in range(9)]
    tall = 100
    ans = []
    for a in range(0, 3):
        tall -= arr[a]
        for b in range(1, 4):
            tall -= arr[b]
            for c in range(2, 5):
                tall -= arr[c]
                for d in range(3, 6):
                    tall -= arr[d]
                    for e in range(4, 7):
                        tall -= arr[e]
                        for f in range(5, 8):
                            tall -= arr[f]
                            for g in range(6, 9):
                                tall -= arr[g]
                                if tall == 0:
                                    ans.append(arr[a])
                                    ans.append(arr[b])
                                    ans.append(arr[c])
                                    ans.append(arr[d])
                                    ans.append(arr[e])
                                    ans.append(arr[f])
                                    ans.append(arr[g])
                                    print(*sorted(ans))
                                    return
                                tall += arr[g]
                            tall += arr[f]
                        tall += arr[e]
                    tall += arr[d]
                tall += arr[c]
            tall += arr[b]
        tall += arr[a]

# seven_small()


def seven_small_2():
    from itertools import combinations
    arr = [int(input()) for _ in range(9)]
    for comb in combinations(arr, 7):
        if sum(comb) == 100:
            ans = sorted(list(comb))
            break
    print(*ans)
seven_small_2()


def seven_small_3():
    arr = [int(input()) for _ in range(9)]
    arr.sort()
    total = 0
    stack = []
    def dfs(s, e, depth, total):
        if depth == 7:
            if total == 100:
                ans = stack

        dfs(idx)

    dfs(0, 9, 0, 0)


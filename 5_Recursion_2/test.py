def recur(idx, S, B):  # S 신맛,  B 쓴맛

    if idx == N:
        ans.append(abs(S - B))
        ##################################################
        res_S_and_B.append([S, B])  # ans 에 들어가는 신맛 & 쓴맛
        ##################################################
        return

    # 재료가 한개일때는 추가하지 않고 넘어가는 조건에 해당안됨
    if N == 1:
        # 재료를 추가함(신맛은 곱, 쓴맛은 합)
        recur(idx + 1, S * food[idx][0], B + food[idx][1])

    if N != 1:
        recur(idx + 1, S * food[idx][0], B + food[idx][1])
        # 재료를 추가하지 않고 넘어감
        recur(idx + 1, S, B)


N = int(input())

food = []
ans = []
##################################################
res_S_and_B = []
##################################################
for _ in range(N):
    a, b = map(int, input().split())
    food.append([a, b])

recur(0, 1, 0)

##################################################
print(res_S_and_B)
##################################################
print(min(ans))

""" 16283번 - Farm """

# 양 식사량 a
# 염소 식사량 b
# n : 양+염소 마리
# w : 전체 식사량
# 양과 염소 각각 마리 구하라
# 1 ≤ a ≤ 1,000, 1 ≤ b ≤ 1,000, 2 ≤ n ≤ 1,000, 2 ≤ w ≤ 1,000,000

""" my solution """

def farm():
    a, b, n, w = map(int, input().split())
    ans = []
    for i in range(1, n):
        if a*i + b*(n-i) == w:
            ans.append((i, n-i))
            if len(ans) >= 2:
                break

    if len(ans) == 2 or len(ans) == 0:
        print(-1)
    else:
        print(*list(*ans))

farm()


""" hint solution """

# 리스트 안쓰고 카운트 변수로 써도 관계없음

def farm_hint():
    a, b, n, w = map(int, input().split())
    cnt = 0
    for i in range(1, n):
        if a * i + b * (n - i) == w:
            cnt += 1
            if cnt == 2:
                break
            sheep = i
            goat = n - i
    if cnt != 1:
        print(-1)
    else:
        print(sheep, goat)

farm_hint()
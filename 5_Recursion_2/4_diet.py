n = int(input())
min_dan, min_ji, min_tan, min_bi = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
min_price = 999999999999
choice = []
ans_choice = []
def recur(idx, dan, ji, tan, bi, price):
    if idx == n:
        if dan >= min_dan and ji >= min_ji and tan >= min_tan and bi >= min_bi:
            global min_price
            global ans_choice
            if min_price > price:
                min_price = price
                ans_choice = []
                ans_choice.extend(choice)
        return
    if sum(arr[idx][:-1]) != 0:
        choice.append(idx+1)
        recur(idx+1, dan+arr[idx][0], ji+arr[idx][1], tan+arr[idx][2], bi+arr[idx][3], price+arr[idx][4])
        choice.pop()
    recur(idx+1, dan, ji, tan, bi, price)

recur(0, 0, 0, 0, 0, 0)

if min_price != 999999999999:
    print(min_price)
    print(*sorted(ans_choice))
else:
    print(-1)


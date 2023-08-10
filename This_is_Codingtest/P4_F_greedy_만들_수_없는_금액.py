""" 그리디 : 4. 만들 수 없는 금액 """

""" 다시 풀어볼 것 : 정답 보고 겨우 품, 잘 이해 안됨 """
def moneyCantMade_hint():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    target = 1
    for a in arr:
        if target >= a :
            target += a
        else:
            print(target)
            break

# moneyCantMade_hint()

def moneyCantMade_ans():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    target = 1
    for a in arr:
        if target < a:
            break
        target += a
    print(target)

# moneyCantMade_ans()


""" 2503 - 숫자 야구 """

def math_baseball():
    n = int(input())
    arr = [list(input().split()) for _ in range(n)]
    ans = 0
    for ys_num in range(100, 1000):
        ys_num = str(ys_num)
        # 영수 수의 세 숫자가 모두 다르지 않으면 패스
        if len(set(ys_num)) != 3 or '0' in ys_num:
            continue
        print('y ' + ys_num)
        count = 0
        for mh_num, strike, ball in arr:
            strike = int(strike)
            ball = int(ball)
            # 스트라이크 개수 맞는지 확인
            new_strike = 0
            for i in range(3):
                if ys_num[i] == mh_num[i]:
                    new_strike += 1
            # 볼 개수 맞는지 확인
            new_ball = 0
            for i in range(3):
                for j in range(3):
                    if i != j and mh_num[i] == ys_num[j]:
                        new_ball += 1
            # 스트라이크 볼 개수 다른거 하나라도 있으면 이번 영수 수는 버리기
            if new_strike != strike or new_ball != ball:
                break
            # 민혁 수 조건 맞으면 카운트 1 증가
            count += 1
        # 모든 민혁 수 조건 맞으면 영수 수 1 증가
        if count == n:
            ans += 1
            # print(ys_num)
    print(ans)

# math_baseball()

def math_baseball_2():
    n = int(input())
    arr = [list(input().split()) for _ in range(n)]
    ans = 0
    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(1, 10):
                if a == b or b == c or c == a:
                    continue
                count = 0
                yh_num = str(100 * a + 10 * b + c)
                for mh_num, strike, ball in arr:
                    tmp_strike = 0
                    tmp_ball = 0
                    if mh_num[0] in yh_num:
                        if mh_num[0] == yh_num[0]: tmp_strike += 1
                        else: tmp_ball += 1
                    if mh_num[1] in yh_num:
                        if mh_num[1] == yh_num[1]: tmp_strike += 1
                        else: tmp_ball += 1
                    if mh_num[2] in yh_num:
                        if mh_num[2] == yh_num[2]: tmp_strike += 1
                        else: tmp_ball += 1
                    if tmp_strike == int(strike) and tmp_ball == int(ball):
                        count += 1
                    else:
                        break
                if count == len(arr):
                    ans += 1
    print(ans)

math_baseball_2()

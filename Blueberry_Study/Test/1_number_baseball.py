""" 2503 - 숫자 야구 """

def num_baseball_idea():

    n = int(input())
    arr = []

    for _ in range(n):
        # q, s, b 에 입력받은 줄 나눠서 넣기
        q, s, b = map(int, input().split())

        # arr 리스트에 [q, s, b] 로 묶은 리스트 넣기
        arr.append([q, s, b])

    count = 0  # 정답

    for i in range(111, 999):
        # i 숫자를 문자열로 바꿈 (자리수 때려고)
        i_num = str(i)

        tmp = 0

        # 세 수가 같으면 안되는 조건 확인
        if i_num[0] == i_num[1] or i_num[1] == i_num[2] or i_num[2] == i_num[0]:
            continue

        for q, s, b in arr:
            # q 숫자를 문자열로 바꿈(자리수 떼려고)
            q_num = str(q)

            # 스트라이크 체크
            strike = 0
            for j in range(3):
                if i_num[j] == q_num[j]:
                    strike += 1
            # 볼 체크
            ball = 0
            for j in range(3):
                if i_num[j] == q_num[(j + 1) % 3]:
                    ball += 1
                if i_num[j] == q_num[(j + 2) % 3]:
                    ball += 1

            # 스트라이크, 볼 개수 일치 체크
            if strike == s and ball == b:
                tmp += 1

        # 일치시 정답 += 1
        if tmp == n:
            count += 1

    print(count)

num_baseball_idea()




def num_baseball_hyein():
    question_list = []  # 입력받은 수의 리스트
    s_list = []
    b_list = []
    count = 0  # 경우의수
    tmp = 0  # 임시변수

    # 스트라이크수 구하기
    def strike(i, question):
        strike = 0

        i_num_1 = i // 100
        i_num_2 = i % 100 // 10
        i_num_3 = i % 10

        q_num_1 = question // 100
        q_num_2 = question % 100 // 10
        q_num_3 = question % 10

        if i_num_1 == q_num_1:
            strike += 1
        if i_num_2 == q_num_2:
            strike += 1
        if i_num_3 == q_num_3:
            strike += 1

        return strike

    # 볼 수 구하기
    def ball(i, question):
        ball = 0

        i_num_1 = i // 100
        i_num_2 = i % 100 // 10
        i_num_3 = i % 10

        q_num_1 = question // 100
        q_num_2 = question % 100 // 10
        q_num_3 = question % 10

        if i_num_1 == q_num_2 or i_num_1 == q_num_3:
            ball += 1
        if i_num_2 == q_num_1 or i_num_2 == q_num_3:
            ball += 1
        if i_num_3 == q_num_2 or i_num_3 == q_num_1:
            ball += 1

        return ball

    # 입력받기
    N = int(input())
    for _ in range(N):
        question, s, b = map(int, input().split())
        question_list.append(question)
        s_list.append(s)
        b_list.append(b)

    # 111~999를 입력받은 수와 스트라이크, 볼 비교
    for i in range(111, 999):
        tmp = 0
        for j in range(N):
            if strike(i, question_list[j]) == s_list[j] and ball(i, question_list[j]) == b_list[j]:
                tmp += 1
        print(tmp, N)
        if tmp == N:
            count += 1

    print(count)

# num_baseball_hyein()




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

# math_baseball_2()

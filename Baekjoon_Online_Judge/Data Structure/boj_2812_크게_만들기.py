""" 2812 : 크게 만들기 """

# 문제
# N자리 숫자가 주어졌을 때, 여기서 숫자 K개를 지워서 얻을 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 K가 주어진다. (1 ≤ K < N ≤ 500,000)

# 둘째 줄에 N자리 숫자가 주어진다. 이 수는 0으로 시작하지 않는다.

# 출력
# 입력으로 주어진 숫자에서 K개를 지웠을 때 얻을 수 있는 가장 큰 수를 출력한다.

#
""" my code """


def makeBig():
    n, k = map(int, input().split())
    ans = []
    count = 0
    for a in input():
        while ans and ans[-1] < a and count < k:
            ans.pop()
            count += 1
        ans.append(a)
    print(''.join(ans)[:n - k])
    # 여기서 엄청 오래 걸렸음
    # print(int(''.join(ans)[:n-k]))
    # 조인 한 결과 int() 씌워서 출력하니까 1700ms, 벗기고 출력하니까 120ms
    # 수가 너무 커져서 그런 것 같음


# makeBig()

# ans = ans[:n-k] 하는 이유는
# 입력이
# 5 1
# 54321
# 인 경우에 숫자가 차례대로 나열되어 있어서 반복문을 다 돌아도 숫자가 빠지지 않는다
# 이게 숫자를 뺄 때마다 1씩 감소해 0까지 도달하는 k에 나타나는데 빠지지 않고 남은
# 숫자의 개수가 k에 저장되기 때문에 ans의 뒤에서부터 k만큼 빼고 출력하면 가장 작은
# 숫자들을 작은 자리수에서 뺄 수 있게 된다.
# 위 코드가 없을 때 출력은 54321 이고, 있을 때는 정답 5432 가 출력된다.

#
""" better code """


def makeBig_b():
    from sys import stdin
    input = stdin.readline
    N, K = map(int, input().split())
    stack = []
    count = 0
    for n in input().rstrip():
        while stack and stack[-1] < n and count < K:
            stack.pop()
            count += 1
        stack.append(n)

    print("".join(stack)[:N - K])

# makeBig_b()

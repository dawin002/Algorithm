""" 6. 2로 몇 번 나누어질까 """

""" my solution """

def div_two():
    a, b = map(int, input().split())
    a -= 1
    res_a = []
    res_b = []
    i = 1
    t = 2 ** i
    while t <= a:
        res_a.append(a // t)
        # print(f"{a} // {t} = {a//t}, two={a//t}")
        i += 1
        t = 2 ** i
    print(res_a)
    i = 1
    t = 2 ** i
    while t <= b:
        res_b.append(b // t)
        # print(f"{b} // {t} = {b // t}, two={b // t}")
        i += 1
        t = 2 ** i
    print(res_b)
    sum_b = res_b[-1] * len(res_b)
    print(sum_b)
    for i in range(len(res_b)-1, 0, -1):
        sum_b += res_b
    # ans = res_b - res_a
    # print(res_a, res_b)
    # print(ans)

div_two()
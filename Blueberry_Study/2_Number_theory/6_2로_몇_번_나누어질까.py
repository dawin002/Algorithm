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
        i += 1
        t = 2 ** i

    for i in range(len(res_a)):
        res_a[i] = (res_a[i] - sum(res_a[i+1::]))*(i+1)

    i = 1
    t = 2 ** i
    while t <= b:
        res_b.append(b // t)
        i += 1
        t = 2 ** i

    for i in range(len(res_b)):
        res_b[i] = (res_b[i] - sum(res_b[i+1::]))*(i+1)

    # print(res_a)
    # print(res_b)
    ans = sum(res_b) - sum(res_a)
    print(ans)

div_two()


""" 1193 : 분수 찾기 """

""" my solution """

def find_div():
    x = int(input())
    y = 0
    for i in range(1, 100000001):
        y += i
        if y >= x:
            n = i
            m = x - y + i
            break
    if n % 2 == 0:
        print(m, '/', n + 1 - m, sep='')
    else:
        print(n + 1 - m, '/', m, sep='')
find_div()


""" answer solution """
def find_div_b():
    x = int(input())

    s = 0
    i = 0
    while x > s:
        i += 1
        s += i

    s = s - i
    if i % 2 == 1:
        a = i - (x - s) + 1
        b = x - s
    else:
        a = x - s
        b = i - (x - s) + 1

    print(f'{a}/{b}')
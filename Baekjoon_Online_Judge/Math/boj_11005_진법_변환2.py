""" 11005 : 진법 변환 2 """

# 정수 n 을 b 진법으로 표현하라

""" my solution """


def jinbeob_2():
    arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'X', 'Y', 'Z']
    n, b = map(int, input().split())
    res = []
    while n > 0:
        res.append(n % b)
        n //= b
    for i in range(len(res)):
        res[i] = arr[res[i]]

    print(''.join(reversed(res)))

jinbeob_2()

""" answer solution """


def jinbeob_ans():
    ans = ''
    x, y = map(int, input().split())
    while x:
        r = x % y
        if 0 <= r <= 9:
            ans += str(r)
        else:
            ans += chr(ord('A') + r - 10)
        x //= y
    print(ans[::-1])
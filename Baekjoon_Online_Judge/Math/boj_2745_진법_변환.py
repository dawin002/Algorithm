""" 2745 : 진법 변환 """

# b 진법 수 st를 10진법으로 출력하라

""" my solution """

def jinbeob():
    st, b = input().split()
    b = int(b)
    i = 0
    ssum = 0
    if b > 10:
        for s in st[::-1]:
            if 65 <= ord(s) <= b+64:
                ssum += b ** i * (ord(s) - 55)
            else:
                ssum += b ** i * int(s)
            i += 1
    else:
        for s in st[::-1]:
            ssum += b ** i * int(s)
            i += 1
    print(ssum)
jinbeob()

""" answer solution """

def jinbeob_ans():
    n, b = input().split()
    print(int(n, int(b)))

def jinbeob_ans2():
    import sys
    c = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n, b = sys.stdin.readline().split()
    ans = 0
    s = 0
    for i in reversed(n):
        ans += (c.index(i)) * (int(b) ** s)
        s += 1
    print(ans)
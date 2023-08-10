""" 2292 : 벌집 """

""" my solution """

def bee_house():
    n = int(input())
    i = 0
    s = 1
    while True:
        s += i*6
        if s >= n:
            break
        i += 1
    print(i+1)
bee_house()
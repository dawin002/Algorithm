""" 1436 : 영화감독 숌 """

# 666이 들어가는 수 중 가장 작은 수부터 n번째의 수는?

""" my solution """

def num_666():
    N = int(input())
    six = 666

    while N:
        if "666" in str(six):
            N -= 1
        six += 1

    print(six - 1)
num_666()
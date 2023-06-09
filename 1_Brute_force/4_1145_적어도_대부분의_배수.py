""" 1145 - 적어도 대부분의 배수 """

def almost_multiple():
    arr = list(map(int, input().split()))
    for i in range(1, 99999999999999):
        count = 0
        for a in arr:
            if i % a == 0:
                count += 1
        if count >= 3:
            print(i)
            break

almost_multiple()
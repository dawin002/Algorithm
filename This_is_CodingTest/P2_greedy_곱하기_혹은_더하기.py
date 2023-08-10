""" 그리디 : 2. 곱하기 혹은 더하기 """

def mulOrPlus():
    arr = list(map(int, input()))
    arr.sort()
    res = arr[0]
    for a in arr[1:]:
        res = max(res+a, res*a)
    print(res)

# mulOrPlus()


def mulOrPlus_ans():
    arr = input()
    arr.sort()
    res = int(arr[0])
    for a in arr[1:]:
        num = int(a)
        if res <= 1 or num <= 1:
            res += num
        else:
            res *= num
    print(res)

# mulOrPlus_ans()
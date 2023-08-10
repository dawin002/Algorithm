""" 구현 문제 : 8. 문자열 재정렬 """

""" my code : 나도 맞음 """

def replaceString():
    arr = sorted(input())
    idx = -1
    for i in range(len(arr)):
        if arr[i] > '9':
            idx = i
            break

    if idx == -1:
        print(sum(list(map(int, arr))))

    elif idx == 0:
        print(''.join(arr))

    else:
        eng = ''.join(arr[idx:])
        num = sum(list(map(int, arr[:idx])))
        print(eng, num, sep='')

replaceString()

""" answer code """
def replaceString_ans():
    arr = input()
    result = []
    value = 0

    for a in arr:
        if a.isalpha():
            result.append(a)
        else:
            value += int(a)

    result.sort()

    if value != 0:
        result.append(str(value))

    print(''.join(result))

replaceString_ans()
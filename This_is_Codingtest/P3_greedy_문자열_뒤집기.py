""" 그리디 : 3. 문자열 뒤집기 """

def reverseString():
    strs = list(map(int, input()))
    pre = strs[0]
    zeroToggle = 0
    oneToggle = 0
    for s in strs[1:]:
        if pre == 1 and s == 0:
            zeroToggle += 1
        if pre != s and s == 1:
            oneToggle += 1
        pre = s
    print(max(zeroToggle, oneToggle))

# reverseString()


def reverseString_2():
    strs = input()
    result = 0
    if strs[0] == '0':
        findS = '01'
    else :
        findS = '10'

    pre = strs[0]
    for s in strs[1:]:
        if pre + s == findS:
            result += 1
        pre = s
    print(result)

# reverseString_2()


def reverseString_3():
    strs = input()
    result = 0
    if strs[0] == '0':
        findS = '01'
    else:
        findS = '10'

    for i in range(len(strs)):
        if strs[i:i+2] == findS:
            result += 1
    print(result)

reverseString_3()
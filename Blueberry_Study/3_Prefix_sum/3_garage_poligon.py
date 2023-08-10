def garage_2():
    n = int(input())
    arr = [0 for _ in range(1003)]

    max_h = 0
    min_l = 9999999
    max_l = -1
    sumi = 0

    for _ in range(n):
        l, h = map(int, input().split())
        arr[l] = h
        max_h = max(max_h, h)
        min_l = min(min_l, l)
        max_l = max(max_l, l)

    height = 0
    for i in range(min_l-2, max_l+2):
        if arr[i] == max_h:
            first_max_pos = i
            break
        if height < arr[i]:
            height = arr[i]
        sumi += height

    height = 0
    for i in range(min_l-2, max_l+2)[::-1]:
        if arr[i] == max_h:
            last_max_pos = i
            break
        if height < arr[i]:
            height = arr[i]
        sumi += height


    sumi += (last_max_pos - first_max_pos + 1) * max_h

    print(sumi)

garage_2()





def garage_3():
    n = int(input())
    arr = []

    max_h = 0
    sumi = 0

    for _ in range(n):
        l, h = map(int, input().split())
        arr.append((l, h))
        max_h = max(max_h, h)
    arr.sort()

    height = 0
    pre_l = 0
    for l, h in arr:
        sumi += height * (l - pre_l)
        pre_l = l
        if h == max_h:
            first_max_pos = l
            break
        if height < h:
            height = h

    height = 0
    pre_l = 1001
    for l, h in arr[::-1]:
        sumi += height * (pre_l - l)
        pre_l = l
        if h == max_h:
            last_max_pos = l
            break
        if height < h:
            height = h

    sumi += (last_max_pos - first_max_pos + 1) * max_h

    print(sumi)

# garage_3()


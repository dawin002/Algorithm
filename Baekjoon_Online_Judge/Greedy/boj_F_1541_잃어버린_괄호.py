""" 1541 : 잃어버린 괄호 """

# 양수, +, - 로 이루어진 식에
# 괄호를 적절히 쳐서 결과를 최소값으로 만들고
# 최소값을 출력하라
# 식 길이 <= 50

""" my solution : Hint (마이너스 뒤에 나오는 +인 애들 모두 묶으면 최소값 나옴) """

# 어우! 복잡해!!! 밑에 코드 보고 배우자!

def my():
    arr = list(input())
    n = len(arr)
    op = ['+', '-']
    new_arr = []
    for i in range(n-1):
        if arr[i] not in op :
            if arr[i+1] not in op:
                arr[i+1] = arr[i] + arr[i+1]
            else:
                new_arr.append(int(arr[i]))
        else:
            new_arr.append(arr[i])

    new_arr.reverse()
    res = new_arr.pop()
    while new_arr:
        o = new_arr.pop()
        num = new_arr.pop()
        if o == '+':
            res += num
        else:
            while new_arr:
                o = new_arr.pop()
                num = new_arr.pop()
                if o == '+':
                    res -= num
                    continue
                else:
                    res

    print(new_arr)


""" ans solution """

# 마이너스를 만났을 때 다음 마이너스 앞까지 모두 더해서 빼주면 최소값 나온다!

def ans():
    arr = input().split('-')
    s = 0
    for i in arr[0].split('+'):
        s += int(i)
    for i in arr[1:]:
        for j in i.split('+'):
            s -= int(j)
    print(s)
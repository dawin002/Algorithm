""" 그리디 : 모험가 길드 """

def fearGuild():

    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort(reverse=True)
    stack = []
    count = 0

    while arr:
        stack.append(arr.pop())
        if len(stack) >= max(stack):
            stack = []
            count += 1

    print(count)

# fearGuild()



def fearGuild_ans():
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()

    result = 0
    count = 0

    for a in arr:
        count += 1
        if count >= a:
            result += 1
            count = 0

    print(result)

fearGuild_ans()
""" 2805 : 농작물 수확하기 """

# n * n 크기 농장
# n은 항상 홀수
# 수확은 농장 크기에 딱맞는 마름모 모양만 가능
# 농장 크기, 농장 지도 주어지면 수익 출력

""" my solution """


def my_solution():
    n = int(input())
    arr = [[0] for _ in range(n + 1)]
    arr[0].extend([0] * n)
    for i in range(1, n + 1):
        arr[i].extend(list(map(int, input())))

    # for line in arr:
    #     print(line)

    res = 0
    half = n // 2 + 1
    for i in range(1, half):
        # print(arr[i][half-(i-1):half+(i-1)+1])
        res += sum(arr[i][half - (i - 1):half + (i - 1) + 1])

    res += sum(arr[half])
    # print(arr[half])

    for i in range(half + 1, n + 1):
        # print(arr[i][i-half+1:n-(i-half)+1])
        res += sum(arr[i][i - half + 1:n - (i - half) + 1])

    return res


""" answer solution """


def ans_solution():
    n = int(input())
    data = [list(map(int, input())) for _ in range(n)]
    start = end = n // 2
    result = 0
    for i in range(n):
        for j in range(start, end + 1):
            result += data[i][j]
        if i < n // 2:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1
    return result


""" main function """


def main():
    t = int(input())

    for tc in range(1, t + 1):
        ans = my_solution()
        print(f"#{tc} {ans}")


main()

""" 1244 : 최대 상금 """

# 나열된 숫자 있음
# 총 n 번 숫자 자리끼리 교환
# 만들 수 있는 최대 수

""" my solution 1 """


def solution():
    arr, c = input().split()
    c = int(c)
    arr = list(map(int, arr))
    arr_max = sorted(arr, reverse=True)
    print(arr)
    if len(arr) == 1:
        ans = arr
    while c > 0:
        idx = -1
        for i in range(len(arr)):
            if arr[i] != arr_max[i]:
                idx = i
                break
        if idx == -1:
            if c % 2 == 0:
                ans = arr
                break
            else:
                arr[-1], arr[-2] = arr[-2], arr[-1]
                ans = arr
                break
        # 만약에 맨뒤에 최대값이 여러개면
        value_max = max(list(arr[idx + 1:]))
        arr.reverse()
        idx_max = len(arr) - arr.index(value_max) - 1
        arr.reverse()
        arr[idx], arr[idx_max] = arr[idx_max], arr[idx]
        print(arr)
        c -= 1
    else:
        ans = arr

    return int(''.join(map(str, ans)))


""" answer solution  """


def change(numbers, cnt):
    global result
    # 현재 숫자 나열 string으로 변환
    temp = ''.join(numbers)
    # 현재 나열이 result[현재 깊이]에 있다면 리턴
    if int(temp) in result[cnt]:
        return
    # 없다면 result[현재 깊이]에 추가
    else:
        result[cnt].append(int(temp))

    # 교환 기회 다 썼으면 리턴
    if cnt == 0:
        return

    n = len(numbers)
    # 현재 숫자 나열에서 교환할 수 있는 모든 경우의 수 점검(재귀)
    for i in range(n):
        for j in range(i + 1, n):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            change(numbers, cnt - 1)
            # 점검하고 나면 되돌려놓기
            numbers[i], numbers[j] = numbers[j], numbers[i]


T = int(input())

for t in range(1, T + 1):
    temp, cnt = input().split()

    numbers = list(temp)
    result = [[] for _ in range(int(cnt) + 1)]

    change(numbers, int(cnt))

    print('#{} {}'.format(t, max(result[0])))



""" anser solution 2 """


def dfs(idx, count):
    global answer
    if count == int(target):
        answer = max(int("".join(nums)), answer)
        return
    for now in range(idx, n):
        for max_idx in range(now + 1, n):
            if nums[now] <= nums[max_idx]:
                nums[now], nums[max_idx] = nums[max_idx], nums[now]
                dfs(now, count + 1)
                nums[now], nums[max_idx] = nums[max_idx], nums[now]
    if not answer and count < int(target):
        rotate = (int(target) - count) % 2
        if rotate:
            nums[-1], nums[-2] = nums[-2], nums[-1]
        dfs(idx, int(target))


for test in range(1, int(input()) + 1):
    nums, target = input().split()
    n = len(nums)
    nums = list(nums)
    answer = 0
    dfs(0, 0)
    print(f'#{test} {answer}')

# 4
# 123 1
# 2737 1
# 32888 2
# 3214777 5

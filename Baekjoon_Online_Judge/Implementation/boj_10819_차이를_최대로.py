""" 10819 : 차이를 최대로 """

# 문제
# N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.

# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|

# 입력
# 첫째 줄에 N (3 ≤ N ≤ 8)이 주어진다. 둘째 줄에는 배열 A에 들어있는 정수가 주어진다. 배열에 들어있는 정수는 -100보다 크거나 같고, 100보다 작거나 같다.

# 출력
# 첫째 줄에 배열에 들어있는 수의 순서를 적절히 바꿔서 얻을 수 있는 식의 최댓값을 출력한다.

#
""" my code"""


def maxDifference():
    from itertools import permutations
    n = int(input())
    arr = list(map(int, input().split()))
    maxD = 0

    for i in permutations(arr):
        s = 0
        for j in range(0, n - 1):
            s += abs(i[j] - i[j + 1])
        maxD = max(maxD, s)

    print(maxD)


#
""" another way : 백트랙킹 """


def maxDifference_2():
    ans = 0
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    maxi, mini = 0, 0
    for i in range(N // 2):
        # print()
        # print('i =', i)
        # print()

        ans += arr[N - 1 - i] - mini
        # print('ans += arr[N-1-i] - mini')
        # print(f'ans += arr[{N-1-i}] - mini')
        # print(f'ans += {arr[N-1-i]} - {mini}')
        # print(f'ans += {arr[N-1-i] - mini}')
        # print(f'ans = {ans}')

        ans += maxi - arr[i]
        # print()
        # print(f'ans += maxi - arr[i]')
        # print(f'ans += maxi - arr[{i}]')
        # print(f'ans += {maxi} - {arr[i]}')
        # print(f'ans += {maxi - arr[i]}')
        # print(f'ans = {ans}')

        maxi, mini = arr[N - 1 - i], arr[i]
        # print()
        # print(f'maxi, mini = arr[N-1-i], arr[i]')
        # print(f'maxi, mini = arr[{N-1-i}], arr[{i}]')
        # print(f'maxi, mini = {arr[N-1-i]}, {arr[i]}')

    if N % 2 == 1:
        ans += max(maxi - arr[N // 2], arr[N // 2] - mini)
    print(ans)
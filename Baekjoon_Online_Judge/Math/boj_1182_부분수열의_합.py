""" 1182 : 부분수열의 합 """

# 문제
# N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다.
# (1 ≤ N ≤ 20, |S| ≤ 1,000,000) 둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다.
# 주어지는 정수의 절댓값은 100,000을 넘지 않는다.

# 출력
# 첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.

#
""" 다른사람 풀이 : 브루트포스 알고리즘 완전탐색 """
""" 풀이 참조 : https://velog.io/@junho918/Algorithm-백준-1182-부분수열의-합-python """


def subSum_bruteforce():
    from itertools import combinations

    N, S = map(int, input().split())
    arr = list(map(int, input().split()))

    count = 0

    for i in range(1, N + 1):
        for comb in combinations(arr, i):
            if sum(comb) == S:
                count += 1

    print(count)


""" 다른사람 풀이 : dfs 알고리즘 완전탐색 """


def subSum_dfs():
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))

    count = [0]

    dfs_subsum(0, 0, N, S, count, arr)

    print(count[0])


def dfs_subsum(idx, sum, N, S, count, arr):
    if idx >= N:
        return

    if sum + arr[idx] == S:
        count[0] += 1

    dfs_subsum(idx + 1, sum, N, S, count, arr)
    dfs_subsum(idx + 1, sum + arr[idx], N, S, count, arr)

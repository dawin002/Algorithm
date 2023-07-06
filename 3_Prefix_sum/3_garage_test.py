import sys


def main():
    N = int(sys.stdin.readline().strip())
    arr = []
    visit = [False] * N
    max_height = 0
    max_idx = -1

    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        arr.append([x, y])

    # 배열 위치순으로 정렬
    arr.sort(key=lambda x: x[0])

    # 가장 큰 기둥 높이와 인덱스 저장
    for i in range(N):
        if max_height < arr[i][1]:
            max_height = arr[i][1]
            max_idx = i

    # 왼쪽부터 저장해준 가장 큰 기둥의 인덱스까지의 면적
    left_max = 0
    left_sum = 0
    for i in range(max_idx + 1):
        if i == 0:
            left_max = arr[i][1]
            left_sum += left_max
            visit[i] = True
            continue
        if left_max < arr[i][1]:
            if arr[i][0] - arr[i - 1][0] >= 2:
                left_sum += left_max * (arr[i][0] - arr[i - 1][0] - 1)
            left_max = arr[i][1]
            left_sum += left_max
            visit[i] = True
        else:
            if arr[i][0] - arr[i - 1][0] >= 2:
                left_sum += left_max * (arr[i][0] - arr[i - 1][0] - 1)
            left_sum += left_max
            visit[i] = True

    # 오른쪽부터 저장해준 가장 큰 기둥의 인덱스까지의 면적
    right_max = 0
    right_sum = 0
    for i in range(N - 1, max_idx - 1, -1):
        if i == N - 1:
            right_max = arr[i][1]
            right_sum += right_max
            visit[i] = True
            continue
        if i == max_idx:
            if arr[i + 1][0] - arr[i][0] >= 2:
                right_sum += right_max * (arr[i + 1][0] - arr[i][0] - 1)
            break
        if right_max < arr[i][1]:
            if arr[i + 1][0] - arr[i][0] >= 2:
                right_sum += right_max * (arr[i + 1][0] - arr[i][0] - 1)
            right_max = arr[i][1]
            right_sum += right_max
            visit[i] = True
        else:
            if arr[i + 1][0] - arr[i][0] >= 2:
                right_sum += right_max * (arr[i + 1][0] - arr[i][0] - 1)
            right_sum += right_max
            visit[i] = True

    sum = left_sum + right_sum
    print(sum)

main()



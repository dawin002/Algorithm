""" 정렬 문제 : 24. 안테나 """

# 일직선상 여러 채의 집
# 안테나 - 집 있는 좌표에만 설치 가능
# 안테나로부터 모든 집의 거리 총합 최소값이 되게 설치
# 안테나 설치 위치 선택

# 1 <= n <= 200,000
# 1 <= 집 좌표 <= 100,000

""" my solution : 완전 탐색 --> 시간 초과 """

def antenna():
    # n = int(input())
    # arr = list(map(int, input().split()))
    arr = [1, 10000, 10001, 10002, 10003]
    n = len(arr)
    min_dist = 1e9
    answer = -1
    for ante in range(n):
        dist = 0
        print(f"antenna : {arr[ante]}")
        for i in range(0, ante):
            print(f"{arr[i]} : {abs(arr[i] - arr[ante])}")
            dist += abs(arr[i] - arr[ante])
        for i in range(ante+1, len(arr)):
            print(f"{arr[i]} : {abs(arr[i] - arr[ante])}")
            dist += abs(arr[i] - arr[ante])
        print(f"distance = {dist}")
        print()
        if min_dist > dist:
            min_dist = dist
            answer = ante
    print(min_dist, arr[answer])

antenna()

""" answer solution """

# 늘 중간값이 답이다. (어떤 상황에서도)

def antenna_ans():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[(n-1)//2])

# antenna_ans()
""" 이진 탐색 문제 : 29. 공유기 설치 """

# N개 집 ( 2 <= n <= 2십만)
# 공유기 C개 설치할 것 ( 2 <= c <= n )
# 한집당 최대 한개 설치
# 인접한 공유기 최대한 멀리 떨어뜨려 설치
# 각 줄 집 좌표 x 입력 ( 1 <= x <= 10억 )
# 가장 인접한 두 공유기 사이 거리 최대값 출력

""" 어떻게 푸는지 감도 안잡힘 """

""" answer solution : """


def wifi_distance():
    n, c = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    arr.sort()  # 이진 탐색을 하기 위한 정렬

    start = 1
    end = arr[-1] - arr[0]
    result = 0

    # 이진 탐색 시작
    while start <= end:
        mid = (start + end) // 2  # mid : 가장 인접한 두 공유기 거리 (gap)
        value = arr[0]
        count = 1
        # 현재의 mid 값(gap)을 이용해 전체 집에 공유기 설치
        for i in range(1, n):
            if arr[i] >= value + mid:
                value = arr[i]
                count += 1
        # c개 이상의 공유기를 설치할 수 있으면 gap 거리 증가
        if count >= c:
            start = mid+1
            result = mid  # 최적의 gap 값 저장
        # c개 이상의 공유기를 설치할 수 없다면 gap 거리 감소
        else:
            end = mid - 1

    print(result)



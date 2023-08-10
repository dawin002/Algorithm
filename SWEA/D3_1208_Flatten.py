""" 1208 : Flatten """

# 100개의 건물
# 1회 동작 : 제일 높은 건물 중 하나의 한 층을 깎아 제일 낮은 건물 중 하나의 한 층을 추가
# 총 n 회 수행
# 건물 층 주어짐

""" my solution : heapq 사용, 근데 안쓰는게 더 빠르더라 """

def my_flatten():
    import heapq

    T = 10
    for test_case in range(1, T+1):
        n = int(input())
        arr = list(map(int, input().split()))
        min_q = []
        max_q = []
        for a in arr:
           heapq.heappush(min_q, a)
           heapq.heappush(max_q, -a)

        while True:
            max_val = -heapq.heappop(max_q)
            min_val = heapq.heappop(min_q)
            if max_val - min_val <= 1 or n == 0:
                ans = max_val - min_val
                break
            n -= 1
            max_val -= 1
            min_val += 1
            heapq.heappush(min_q, min_val)
            heapq.heappush(max_q, -max_val)

        print(f"#{test_case} {ans}")

"""" faster solution : max(), min() 사용 """

def flatten_max_min():

    for test_case in range(1, 11):
        counter = int(input())
        boxs = list(map(int, input().split()))
        count = 0

        while True:
            # 제한 횟수 넘으면
            if counter <= count:
                break

            # 평탄화 작업 끝나면
            if boxs[boxs.index(max(boxs))] - boxs[boxs.index(min(boxs))] <= 1:
                break

            # 가장 큰 값에서 1빼고 가장 작은 값에 1 추가
            boxs[boxs.index(max(boxs))] -= 1
            boxs[boxs.index(min(boxs))] += 1
            count += 1

        result = boxs[boxs.index(max(boxs))] - boxs[boxs.index(min(boxs))]

        print(f'#{test_case} {result}')

# 1 13
# 2 32
# 3 54
# 4 25
# 5 87
# 6 14
# 7 39
# 8 26
# 9 13
# 10 29

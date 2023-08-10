""" 정렬 문제 : 26. 카드 정렬하기 """

# 정렬된 두 묶음의 숫자 카드
# 두 묶음 카드의 수 각각 a, b 개
# 두 묶음 합쳐서 하나로 만드려면 a + b 번 비교 필요
# 여러 묶음 카드 개수 주어질 때
# 모두 합치기 위한 최소 비교 횟수?

""" my solution : 틀렸습니다? """

# 오름차순 해서 풀면 정답일 것이다

def sort_card():
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    arr.sort()

    card_sum = arr[0]
    total_sum = 0
    for i in range(1, n):
        card_sum += arr[i]
        total_sum += card_sum

    print(total_sum)

# sort_card()

""" my solution 2 : 수학으로 풀기? ==> 틀렸습니다 """

def sort_card_2():
    import sys
    n = int(sys.stdin.readline().rstrip())
    arr = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
    arr.sort()
    answer = -arr[0]
    for i in range(n):
        answer += arr[i] * (n-i)
    print(answer)
# sort_card_2()


""" my solution 3 : 계수정렬이면 만족하겠니? """
def sort_card_3():
    import sys
    n = int(sys.stdin.readline())
    arr = [0] * 1001
    for _ in range(n):
        arr[int(sys.stdin.readline().rstrip())] += 1

    answer = 0
    count = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            for _ in range(arr[i]):
                answer += i * (n - count)
                count += 1

    for f in range(len(arr)):
        if arr[f] != 0:
            first = f
            break

    answer -= first
    print(answer)

# sort_card_3()


""" my solution 4 : 힌트 ( 항상 가장 작은 두 묶음을 합쳐야 함 )"""

def sort_card_hint():
    import sys
    import heapq
    n = int(sys.stdin.readline())
    if n == 1:
        print(0)
        return

    q = []
    for _ in range(n):
        heapq.heappush(q, int(sys.stdin.readline()))

    answer = 0
    while len(q) > 1:
        a, b = heapq.heappop(q), heapq.heappop(q)
        answer += a + b
        heapq.heappush(q, a + b)
    print(answer)

sort_card_hint()


""" answer  solution : 조금 다름 """

def sort_card_ans():
    import heapq
    n = int(input())
    heap = []
    for i in range(n):
        heapq.heappush(heap, int(input()))

    result = 0

    # 책 풀이 특징 : while 조건식을 len(heap) != 1 로 둬서 n=1인 케이스까지 처리할 수 있음
    while len(heap) != 1:
        # (내 코드 사용) heappop()한 두 원소 더한 값 sum_a_b 변수 하나로 사용
        sum_a_b = heapq.heappop(heap) + heapq.heappop(heap)
        result += sum_a_b
        heapq.heappush(heap, sum_a_b)

    print(result)
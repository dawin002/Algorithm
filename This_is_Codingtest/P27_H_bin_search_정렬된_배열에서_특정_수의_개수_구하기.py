""" 이진 탐색 문제 : 27. 정렬된 배열에서 특정 수의 개수 구하기 """

# n 개 원소 수열 오름차순
# x의 회수 구하라
# O(logN)으로 구현하지 않으면 시간초과

""" my solutions : Fail ( 시간 복잡도 O(logN) 못 맞춤 ) """

def get_num_x():
    n, target = map(int, input().split())
    arr = list(map(int, input().split()))
    start = 0
    end = n-1
    idx = -1
    while start < end:
        mid = (start + end) // 2
        if arr[mid] == target:
            idx = mid
            break
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    if idx != -1:
        count = 1
        i = 1
        while idx+i < n:
            if arr[idx+i] == target:
                count += 1
                i += 1
            else:
                break
        i = 1
        while idx-i >= 0:
            if arr[idx-i] == target:
                count += 1
                i += 1
            else:
                break
        print(count)

    else:
        print(-1)

# get_num_x()


""" my solution + hint : """

def get_num_x_hint():
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))

    target = x

    def first(start, end):
        if end < start:
            return -1
        mid = (start + end) // 2
        if (mid == 0 or arr[mid-1] != target) and arr[mid] == target:
            return mid
        elif target <= arr[mid]:
            return first(start, mid-1)
        else:
            return first(mid+1, end)

    def last(start, end):
        if end < start:
            return -1
        mid = (start + end) // 2
        if (mid == n-1 or arr[mid+1] != target) and arr[mid] == target:
            return mid
        elif arr[mid] <= target:
            return last(mid+1, end)
        else:
            return last(start, mid-1)

    idx_first = first(0, n-1)
    # first 없으면 바로 반환
    if idx_first == -1:
        print(-1)
        return

    idx_last = last(0, n-1)

    print(idx_last - idx_first + 1)
    return

get_num_x_hint()

""" 딴 건 필요 없고, 책의 이진 탐색 함수 first(), last() 구현 방식 """

# 더 밑에 bisect() 함수 사용 방법도 꼭 봐야됨!!!

# first_ans(arr, x, 0, n-1)
def first_ans(arr, tar, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 해당 값을 가지는 원소 중에서 가장 왼쪽의 원소인 경우에만 인덱스 반환
    if (mid == 0 or tar > arr[mid-1]) and arr[mid] == tar:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 확인
    elif arr[mid] >= tar:
        return first_ans(arr, tar, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return first_ans(arr, tar, mid+1, end)


# last_ans(arr, x, 0, n-1)
def last_ans(arr, tar, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 해당 값을 가지는 원소 중에서 가장 오른쪽의 원소인 경우에만 인덱스 반환
    if (mid == len(arr)-1 or tar < arr[mid+1]) and arr[mid] == tar:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif arr[mid] > tar:
        return last_ans(arr, tar, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 크거나 같은 경우 오른쪽 확인
    else:
        return last_ans(arr, tar, mid+1, end)

""" book solution : 파이썬 내장 함수 bisect 사용 방식 """

# bisect : 이진 탐색 파이썬 라이브러리
# bisect_left(), bisect_right() : 정렬된 리스트 내에 특정 값이 삽입될 수 있는 가장 왼쪽, 오른쪽 인덱스 반환
# count_by_range() : 사용자 함수, bisect_left(), bisect_right() 이용
#                    리스트 내에 특정 값이 들어갈 수 있는 범위의 원소 개수 반환

def get_num_x_ans():
    from bisect import bisect_left, bisect_right

    def count_by_range(arr, d1, d2):
        left_idx = bisect_left(arr, d1)
        right_idx = bisect_right(arr, d2)
        return right_idx - left_idx

    n, x = map(int, input().split())
    arr = list(map(int, input().split()))

    count = count_by_range(arr, x, x)

    if count == 0:
        print(-1)
    else:
        print(count)
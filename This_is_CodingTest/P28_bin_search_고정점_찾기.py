""" 이진 탐색 문제 : 28. 고정점 찾기 """

# 고정점 : 그 값이 인덱스와 동일한 원소
# n개의 수열, 서로 다른 원소 (1 <= n <= 1백만)
# 오름차순 정렬
# 고정점 있다면 출력, 없다면 -1 출력
# 시간복잡도 O(logN)

""" my solution """

def fixed_point():
    n = int(input())
    arr = list(map(int, input().split()))

    def bin_index(start, end):
        if start > end:
            return -1
        mid = (start + end) // 2
        if mid == arr[mid]:
            return mid
        elif mid > arr[mid]:
            return bin_index(mid + 1, end)
        else:
            return bin_index(start, mid - 1)

    result = bin_index(0, n-1)
    print(result)

fixed_point()


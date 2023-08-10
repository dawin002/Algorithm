""" 이진 탐색 : Binary Search """

# 카테고리
#     순차 탐색
#     이진 탐색
#     이진 탐색 트리
#     파라메트릭 서치


""" 순차 탐색 : Sequential Search """

# 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
# 정렬되지 않은 리스트에서 데이터를 찾아야 할 때 사용
# List 자료형의 메서드인 count()가 내부적으로 순차탐색 수행
# 시간 복잡도 : O(N)

def sequential_search(target, array):
    n = len(array)
    for i in range(n):
        if array[i] == target:
            return i + 1


""" 이진 탐색 : Binary Search """

# 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해 원하는 데이터를 찾는 방법
# 시작점, 끝점, 중간점 3개 변수 사용
# 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘
# 시간 복접도 : O(logN)

# 처리해야 할 데이터의 개수나 값이 1000만 단위를 넘어가면 이진탐색을 사용해야 풀 수 있는 경우가 많음


# 이진탐색 구현 : 재귀함수
def bin_search_recur(array, target, start, end) :
    if start > end:
        return '존재하지 않습니다'
    middle = (end+start)//2
    if target == array[middle]:
        return middle
    elif target < array[middle]:
        return bin_search_recur(array, target, start, middle - 1)
    else:
        return bin_search_recur(array, target, middle + 1, end)


# 이진탐색 구현 : 반복문
def bin_search_for(array, target):
    start = 0
    end = len(array)-1
    while start <= end:
        middle = (end+start)//2
        if target == array[middle]:
            return middle
        elif target < array[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return '존재하지 않습니다'


""" 이진 탐색 트리 """

# 특징
#     부모 노드보다 왼쪽 자식 노드가 작다
#     부모 노드보다 오른쪽 자식 노드가 크다


""" 파라메트릭 서치 : Parametric Search"""

# 최적화 문제를 *결정 문제로 바꾸어 해결하는 기법
# * 결정 문제 : '예' 혹은 '아니오' 로 답하는 문제
# 원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제에 주로 사용

# ex) C7_3_떡볶이_떡_만들기
#     n 개 떡, 총 길이 m 만큼의 떡 필요, 각 떡 높이 다름, 밑에서부터 얼마 남기고 잘라야 남은 떡 최대?
#     : 범위 내에서 조건을 만족하는 가장 큰 값을 찾는 최적화 문제
#       --> 이진 탐색으로 결정 문제를 해결하면서 범위를 좁혀나가면 됨
#       : 조건을 만족하는 적절한 큰 값인가? 에 대한 조건 만족 여부(예/아니오)에 따라
#         이진탐색으로 탐색 범위를 절반씩 좁혀나가면서 최적의 해를 구하면 됨

def cut_ddeok_para_search(n, need, arr):
    start = 0
    end = max(arr)
    result = 0
    while start <= end:
        total_ddeok = 0
        mid = (start + end) // 2
        for ddeok in arr:
            if ddeok > mid:
                total_ddeok += ddeok - mid
        if total_ddeok < need:
            end = mid - 1
        else:
            result = mid  # 최대한 덜 잘랐을 때가 정답이므로 절단기 높이 최대값 갱신
            start = mid + 1
    return result




def bin_search_main():
    n = 10
    arr1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    print(f"\narr1 =", arr1, '\n')
    print('binary search by recursive')
    print('find 7 :', bin_search_recur(arr1, 7, 0, n-1))
    print('find 8 :', bin_search_recur(arr1, 8, 0, n-1))
    print()
    print('binary search by for')
    print('find 5 :', bin_search_for(arr1, 5))
    print('find 6 :', bin_search_for(arr1, 6))

bin_search_main()



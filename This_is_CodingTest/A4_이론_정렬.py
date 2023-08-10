""" 정렬 : Sort """

# 데이터를 특정 기준에 따라 순서대로 나열하는 것

# 카테고리
#     선택 정렬
#     삽입 정렬
#     퀵 정렬
#     파이썬 기본 정렬 라이브러리

# 어떤 유형 있을까?
# 1. 정렬 라이브러리로 풀 수 있는 문제
#     : 단순히 정렬 기법을 알고 있는지 물어보는 문제. 기본 정렬 라이브러리 사용
# 2. 정렬 알고리즘의 원리에 대해 물어보는 문제
#     : 선택 정렬, 삽입 정렬, 퀵 정렬 등 원리를 알아야 풀 수 있는 문제
# 3. 더 빠른 정렬이 필요한 문제
#     : 퀵 정렬로는 풀 수 없어 계수 정렬 등 다른 정렬 알고리즘을 사용하거나 문제에서 기존에 알려진
#       알고리즘의 구조적인 개선을 거쳐야 풀 수 있는 문제


""" 선택 정렬 : Selection Sort """

# 가장 작은 데이터를 선택해 맨 앞 데이터와 바꾸고, 그다음 작은 데이터를 선택해 앞에서 두번째 데이터와 바꾸는 방식
# 매번 가장 작은 것을 선택
# 가장 작은 데이터를 앞으로 보내는 과정을 N-1번 반복하면 정렬이 완료
# 시간 복잡도 : O(N^2)

def selection_sort():
    arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    for i in range(len(arr)):
        min_i = i
        for j in range(i+1, len(arr)):
            if arr[min_i] > arr[j]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]

    print(arr)
# selection_sort()


""" 삽입 정렬 : Insertion Sort """

# 특정한 데이터를 적절한 위치에 삽입
# 특정 데이터가 적절한 위치에 들어가기 전에, 그 앞까지의 데이터는 이미 정렬되어 있다고 가정
# 특정 데이터가 삽입될 차례가 되면, 그 인덱스부터 왼쪽으로 한 칸씩 이동하며
# 자신보다 작은 데이터를 만나면 멈춤(발견한 작은 데이터 뒤에 삽입)
# 시간 복잡도 : O(N^2)
#            단, 최선의 경우 O(N) : 현재 리스트가 거의 정렬되어 있는 상태라면 매우 빠르게 동작

def insertion_sort():
    arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break

    print(arr)
# insertion_sort()


""" 퀵 정렬 : Quick Sort """

# 재귀 함수 사용
# 기준을 잡고 기준보다 큰 데이터와 기준보다 작은 데이터의 위치를 교환, 리스트를 분할하는 동작을
# 재귀함수 매개변수로 호출되는 리스트의 데이터가 1개가 될 때까지 재귀적으로 반복
# 시간 복잡도 : 평균 O(NlogN)
#            최악의 경우 O(N^2) : 데이터가 이미 정렬되어 있는 경우

# 동작 원리
    # 1. 현재 리스트의 가장 앞 값을 피벗(기준)으로 설정
    # 2. 피벗보다 큰 데이터와 피벗보다 작은 데이터를 각각 찾아 교환
    # 3. 큰 데이터와 작은 데이터 찾는 인덱스 변수가 서로 엇갈리면 피벗과 작은 데이터 교환
    # 4. 피벗보다 왼쪽인(작은) 리스트, 피벗보다 오른쪽인(큰 수들의) 리스트로 현재 리스트를 2개로 나눔
    # 5. 2개로 나눈 각각의 리스트에 대하여 1~5 과정 재귀적 수행 (현재 리스트의 데이터가 1개인 경우 재귀 종료)

def quick_sort_main():
    arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        tail = arr[1:]  # 피벗을 제외한 리스트

        left = [x for x in tail if x <= pivot]  # 분할된 왼쪽 리스트
        right = [x for x in tail if x > pivot]  # 분할된 오른쪽 리스트

        # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 재귀적으로 정렬 수행 후 전체 리스트 반환
        return quick_sort(left) + [pivot] + quick_sort(right)

    print(quick_sort(arr))
# quick_sort_main()


""" 계수 정렬 : Count Sort """

# 별도의 리스트를 선언하고, 데이터를 인덱스로 하는 원소의 값을 1씩 증가시켜
# new_arr[data] = count(data) 와 같은 원소를 가지는 new_arr 을 만드는 방식
# 만든 new_arr의 인덱스 값을 그 인덱스에 저장된 값 만큼 출력하면 정렬 완료

# 모든 데이터가 양의 정수이고, 데이터의 크기 범위가 제한되어 정수 형태로 표현 가능할 때만 사용 가능
# 일반적으로 가장 큰 데이터와 가장 작은 데이터의 차이가 1백만을 넘지 않을 때 효과적으로 사용 가능
# 이유는 모든 범위를 담을 수 있는 크기의 리스트를 선언해야 하기 때문

# 시간 복잡도 : O(N + K)  (K = max(arr))
# 공간 복잡도 : O(N + K)  (데이터의 크기가 많이 중복되어 있을수록(동일 값이 많을수록) 유리함)

def count_sort():
    arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    count_arr = [0] * (max(arr) + 1)

    for i in range(len(arr)):
        count_arr[arr[i]] += 1

    sorted_arr = []

    for i in range(len(count_arr)):
        for j in range(count_arr[i]):
            sorted_arr.append(i)

    print(sorted_arr)
    return sorted_arr
# count_sort()


""" 파이썬 기본 정렬 라이브러리 """

# sort(), sorted()
# 병합 정렬 기반으로 만들어짐
# 일반적으로 퀵 정렬보다 느리지만, 최악의 경우에도 O(NlogN) 보장

# sorted() 는 set(집합)이나 dict(사전) 자료형 입력 받아도 리스트 자료형으로 반환

def phthon_sort():
    arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    arr.sort()         # arr 원본 정렬, 반환 x
    arr = sorted(arr)  # arr 사본 정렬 후 리스트 반환

    # reverse : 뒤집기 (내림차순 정렬할 때 이용)
    arr.sort(reverse=True)  # 내림차순 정렬

    # key : 정렬 기준
    arr.sort(key=lambda x: x[1])  # 원소의 [1]번째 인덱스 기준으로 정렬

    def setting(data):
        return data[1]
    arr.sort(key=setting)  # 람다 함수 안쓰고 이렇게도 가능 (위 key와 동일 기능)
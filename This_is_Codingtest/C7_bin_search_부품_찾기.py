""" 2. 부품 찾기 - 반복문 이진 탐색 """


# 이진 탐색은 빠르나 sort()의 시간 복잡도가 N x logN 으로 오래 걸릴 수도?

def bin_search_for(tar, arrN):
    start = 0
    end = len(arrN) - 1
    while start <= end:
        mid = (start + end) // 2
        if arrN[mid] == tar:
            return 'yes'
        elif arrN[mid] > tar:
            end = mid - 1
        else:
            start = mid + 1
    return 'no'


def findMachine_binary():
    n = int(input())
    arrN = list(map(int, input().split()))
    arrN.sort()
    m = int(input())
    arrM = list(map(int, input().split()))
    for tar in arrM:
        print(bin_search_for(tar, arrN), end=' ')


""" 2. 부품 찾기 - 계수 정렬 """


# 부품 번호가 모두 양의 정수고 부품 수까지 확인 하려면 계수 정렬이 베스트

def findMachine_GyeSuSort():
    n = int(input())
    arrN = list(map(int, input().split()))
    maxN = max(arrN)
    m = int(input())
    arrM = list(map(int, input().split()))
    arrG = [0] * (maxN + 1)
    for a in arrN:
        arrG[a] += 1
    for b in arrM:
        if arrG[b] != 0:
            print('yes', end=' ')
            arrG[b] -= 1
        else:
            print('no', end=' ')


# findMachine_GyeSuSort()

""" 2. 부품 찾기 - 집합 자료형 이용 """


# 코드 간결성 중요시 + 정렬 안쓰려면 set()으로 집합 자료형 쓰는 것도 가능

def findMachine_set():
    n = int(input())
    arrN = set(map(int, input().split()))
    m = int(input())
    arrM = list(map(int, input().split()))
    for a in arrM:
        if a in arrN:
            print('yes', end=' ')
        else:
            print('no', end=' ')
    print(arrN)

# findMachine_set()

# input
# 5
# 8 3 7 9 5 7
# 3
# 5 7 7 7

""" 3. 떡볶이 떡 만들기 - """

# 떡 잘라서 팜
# 손님은 떡 잘린 윗부분 만큼 가져감
# 절단기는 남는 떡 높이 설정 가능
# 손님 요청 떡 길이 맞추는 절단기 세팅 높이 최대값
# n = 떡 개수
# m = 손님 요청 떡 길이
# arr = 현재 떡 길이 정보


""" 내 코드 """


# 리뷰
# 별로 안좋은 방법인 것 같음
# 1~10억인 떡 길이 만큼 크기의 배열을 만들어야해서
# 배열에 넣는 작업이 10억번이 넘어갈 수도 있음
# 데이터 크면 백퍼 시간 초과

def cut_ddeok():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    maxA = max(arr)
    arrG = [0] * (maxA + 1)

    for a in arr:
        for i in range(1, a + 1):
            arrG[i] += 1

    for j in range(maxA - 1, 0, -1):
        arrG[j] += arrG[j + 1]

    start = 1
    end = maxA + 1
    ans = maxA + 1
    while start <= end:
        mid = (start + end) // 2
        if arrG[mid] == m:
            ans = mid
            break
        elif arrG[mid] < m:
            end = mid - 1
        else:
            ans = mid
            start = mid + 1

    print(ans - 1)


# cut_ddeok()


""" 떡볶이 떡 자르기 정답 """


def cut_ddeok_ans():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    start = 0
    end = max(arr)

    res = 0
    while start <= end:
        total = 0
        mid = (start + end) // 2
        for ddeok in arr:
            if ddeok > mid:
                total += ddeok - mid
        if total < m:
            end = mid - 1
        else:
            res = mid
            start = mid + 1

    print(res)

# cut_ddeok_ans()

""" DP 문제 : 34. 병사 배치하기 """

# n 명의 병사 나열
# 각각 전투력 다름
# 전투력 내림차순 되도록 병사 열외
# 열외시켜야 하는 병사 최소값

""" answer solution : 감 잡음 """

# 전형적인 '가장 긴 증가하는 부분 수열 (LIS)' 문제
# LIS 푸는 방식을 전혀 몰랐음
# 아래 순서로 품
# 주어진 리스트 arr, 그 길이 n
# n 길이의 dp 리스트 전체 1로 초기화 (원소 각각이 길이 1의 수열이니까)
# 첫 번째 반복문 i : range(1, n) 탐색하면서 dp[i] 갱신할 것
#   두 번째 반복문 j : range(0, i) 탐색하면서 arr[i] 보다 작은 arr[j] 찾을것
#       찾은 arr[j] 의 arr[j] 밑으로 달린 '가장 긴 증가 부분수열'을 arr[i]가 흡수 (더 크니까)
#       dp[i]에 길이를 dp[i] 와 dp[j]+1 중 최대값으로 갱신함으로써 부분수열 흡수
# dp는 결국 각 원소 아래에 달린 '가장 긴 증가하는 부분수열'의 길이 리스트
# dp의 max 값 받으면 전체 arr에서 가장 긴 증가하는 부분수열의 길이 찾을 수 있음

def soldier_out():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.reverse()

    dp = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j]+1)

    print(n - max(dp))

soldier_out()

# 7
# 15 11 4 8 5 2 4
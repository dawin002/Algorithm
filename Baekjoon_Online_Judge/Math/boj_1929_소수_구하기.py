""" 1929 : 소수 구하기 """

# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

#
""" my code """


def prime_number():
    M, N = map(int, input().split())

    # 0 ~ 50중 소수를 구하기 위한 함수
    arr = [True] * (N + 1)  # 특정 수가 지워졌는지 아닌지 확인하기 위한 배열
    arr[0] = False
    arr[1] = False

    for i in range(2, N + 1):
        if arr[i] == True:  # 특정 수가 지워지지 않았다면 (소수여서)
            j = 2

            while (i * j) <= N:
                arr[i * j] = False  # i의 배수의 값을 False로 지워준다.
                j += 1

    for i in range(M, len(arr)):
        if arr[i] == True:
            print(i)

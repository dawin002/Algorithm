""" 2. 소수 찾기 """

# 주어진 n개 수 중 소수가 몇 개인지 출력
# n <= 100 , 1 <= 각 수 <= 1000

def find_prime():
    n = int(input())
    arr = list(map(int, input().split()))

    ans = 0
    ans -= arr.count(1)
    for a in arr:
        prime = True
        for i in range(2, a):
            if a % i == 0:
                prime = False
        if prime:
            ans += 1

    print(ans)

find_prime()



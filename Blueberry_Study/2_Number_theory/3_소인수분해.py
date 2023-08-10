""" 3. 소인수분해 """

# 주어진 n 을 소인수분해해서 출력
# n <= 1천만
# 소인수분해 결과 한 줄에 하나씩 오름차순 출력

def division_self():
    n = int(input())
    while n > 1:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                print(i)
                n = n // i
                break
        else:
            print(n)
            break
division_self()


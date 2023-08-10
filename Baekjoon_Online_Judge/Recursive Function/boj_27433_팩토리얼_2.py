""" 27433 : 팩토리얼 2"""

# n! 출력

def factorial_2():

    def facto(n):
        if n <= 1:
            return 1
        return n * facto(n-1)

    n = int(input())

    print(facto(n))

factorial_2()
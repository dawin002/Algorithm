""" 10870 : 피보나치 수 5 """

# 피보나치 수열 : if a > 1 : a[i] = a[i-1] + a[i-2]

def fibonacci_5():

    def fibo(n):
        if n <= 1:
            return n
        return fibo(n-1) + fibo(n-2)

    n = int(input())

    print(fibo(n))

fibonacci_5()

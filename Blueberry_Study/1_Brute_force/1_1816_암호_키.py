""" 1816 - 암호 키 """

def pass_key():
    n = int(input())
    for i in range(n):
        num = int(input())
        ans = 'YES'
        for i in range(2, 1000000):
            if num % i == 0:
                ans = 'NO'
                break
        print(ans)
pass_key()
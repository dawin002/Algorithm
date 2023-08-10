""" 25501 : 재귀의 귀재 """

# 아래 함수로 펠린드롬 알 수 있음
# 펠린드롬이란 반전시켜도 동일한 단어
# 재귀함수의 호출 회수를 출력

def recursion_noisrucer():

    def recursion(s, l, r):
        count[0] += 1
        if l >= r:
            return 1
        elif s[l] != s[r]:
            return 0
        else:
            return recursion(s, l + 1, r - 1)

    def isPalindrome(s):
        return recursion(s, 0, len(s) - 1)

    n = int(input())
    for _ in range(n):
        s = input()
        count = [0]
        print(isPalindrome(s), count[0])

recursion_noisrucer()


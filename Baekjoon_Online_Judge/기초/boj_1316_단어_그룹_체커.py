""" 1316 : 단어 그룹 체커 """

""" my solution """

def my_solution():
    import sys
    input = sys.stdin.readline

    count = 0
    for _ in range(int(input())):
        st = list(input().rstrip())
        s_set = set()
        pre = ''
        break_flag = False
        while st:
            s = st.pop()
            if pre != s:
                if s not in s_set:
                    s_set.add(s)
                    pre = s
                else:
                    break_flag = True
                    break
        if not break_flag:
            count += 1
    print(count)


""" answer solution """


def better_solution():
    N = int(input())
    cnt = N
    for i in range(N):
        word = input()
        for j in range(0, len(word) - 1):
            if word[j] == word[j + 1]:
                pass
            elif word[j] in word[j + 1:]:
                cnt -= 1
                break
    print(cnt)


def best_solution():
    result = 0
    for i in range(int(input())):
        word = input()
        if list(word) == sorted(word, key=word.find):
            result += 1
    print(result)

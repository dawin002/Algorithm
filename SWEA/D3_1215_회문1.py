""" 1215 : 회문1 """

# 회문 : ABCBA 처럼 앞뒤로 읽어도 똑같은 단어
# 8x8 배열에서 n 길이의 (가로 or 세로) 회문 개수 구하기

""" my solution """

def fb_same_word():
    n = int(input())
    arr = [list(input()) for _ in range(8)]
    # for line in arr:
    #     print(line)
    res = 0

    for i in range(8):
        for j in range(8):
            if j+n <= 8:
                s = ''.join(arr[i][j:j + n])
                # print(s, s[::-1])
                if s == s[::-1]:
                    res += 1

            if i+n <= 8:
                s = ''.join([arr[x][j] for x in range(i, i + n)])
                # print(s, s[::-1])
                if s == s[::-1]:
                    res += 1

    return(res)

""" main function """

T = 10

for tc in range(1, T+1):
    res = fb_same_word()
    print(f"#{tc} {res}")


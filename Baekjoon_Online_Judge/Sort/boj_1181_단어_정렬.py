""" 1181 : 단어 정렬 """

# 길이 짧은 순 -> 사전순 정렬

""" my solution """

def short_dic_sort():
    import sys
    input = sys.stdin.readline
    n = int(input())
    arr = list(set([input().rstrip() for _ in range(n)]))
    print('\n'.join(sorted(arr, key=lambda x: (len(x), x))))

short_dic_sort()



""" my solution 2 : readlines() """

def short_dic_sort_2():
    import sys
    arr = list(set(sys.stdin.readlines()[1:]))
    arr.sort(key=lambda x: (len(x), x))
    print("".join(arr))  # 왜 "".join()이지??

# short_dic_sort_2()
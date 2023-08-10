""" 2751 : 수 정렬하기 2 """

""" my solution """

def sort_num_2():
    import sys
    input = sys.stdin.readline
    arr = [False] * 2000001
    for _ in range(int(input())):
        arr[int(input())+1000000] = True
    for i in range(2000001):
        if arr[i]:
            print(i-1000000)
sort_num_2()
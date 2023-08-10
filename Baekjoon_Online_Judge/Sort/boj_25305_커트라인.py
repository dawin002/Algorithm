""" 25305 : 커트라인 """

""" my solution """

def cut_line():
    import sys
    input = sys.stdin.readline
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    print(arr[k-1])
cut_line()
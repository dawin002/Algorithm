import sys

input = sys.stdin.readline

def bin_search(start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            start = mid + 1
            continue
        else:
            end = mid - 1
            continue
    return 0

n = int(input())
arr = sorted(list(map(int, input().split())))

m = int(input())
arr2 = list(map(int, input().split()))

answer = []

for target in arr2:
    answer.append(bin_search(0, n-1, target))

print(*answer)
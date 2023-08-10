import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
target = int(input())

arr.sort()

start = 0
end = n-1

count = 0

while start < end:
    now = arr[start] + arr[end]
    if now == target:
        count += 1
        start += 1
        end -= 1
    elif now < target:
        start += 1
    elif now > target:
        end -= 1

print(count)
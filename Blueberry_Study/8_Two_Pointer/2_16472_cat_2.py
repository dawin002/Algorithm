import sys

n = int(input())
arr = list(sys.stdin.readline().rstrip())

start = 0
end = 0
max_len = 0

chars = set()

while start <= end < len(arr):
    chars.add(arr[end])

    if len(chars) <= n:
        max_len = max(max_len, end - start + 1)
        end += 1

    elif len(chars) > n:
        start += 1
        end = start
        chars = set(arr[start])

print(max_len)
max_height, n = map(int, input().split())
arr = list(map(int, input().split()))

max_h = max(arr)

result = 0

height = 0
for i in range(n):
    result += height
    if arr[i] == max_h:
        left_max_i = i
        break
    if height < arr[i]:
        height = arr[i]

height = 0
for i in range(n)[::-1]:
    result += height
    if arr[i] == max_h:
        right_max_i = i
        break
    if height < arr[i]:
        height = arr[i]

result += (right_max_i - left_max_i + 1) * max_h
result -= sum(arr)

print(result)
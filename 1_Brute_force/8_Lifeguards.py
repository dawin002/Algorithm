n = int(input())
time = [0 for _ in range(1001)]
guards = []
for _ in range(n):
    start, end = map(int, input().split())
    for i in range(start, end):
        time[i] += 1
    guards.append((start, end))

max_time = 0

for start, end in guards:
    count = 0
    for i in range(start, end):
        time[i] -= 1
    # print(f"start:{start}, end={end}")
    # print(time)
    for i in range(1001):
        if time[i] != 0:
            count += 1
    max_time = max(max_time, count)
    for i in range(start, end):
        time[i] += 1

print(max_time)
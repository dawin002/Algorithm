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

    # 블루베리님 방식과 다른 부분
    elif len(chars) > n:  # 현재 포함된 문자 종류가 n개 보다 많으면
        while len(set(arr[start:end+1])) > n:  # n개가 될 때까지 start 계속 전진시키기
            start += 1
        chars = set(arr[start:end+1])  # 현재 포함된 문자 종류 갱신

print(max_len)
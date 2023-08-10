n = int(input())
arr = [0] + list(map(int, input().split()))

for i in range(1, n+1):
    arr[i] = max( arr[i] + arr[i-1] , arr[i] )

ans = max(arr[1::])

print(ans)

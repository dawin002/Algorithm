# input a, b -> return min(a + b + x/2, x)
# 꽉찬 통 최대한 많이 만드는게 목표

# a, b 합쳐서 반보다 작으면 작은거끼리 합쳐!

n, x = map(int, input().split())
arr = sorted(list(map(int, input().split())))

count = 0
small_count = 0
# small_arr = []

s = 0
e = len(arr) - 1

while s < e:
    if arr[s] >= x:
        # print('over :', arr[s])
        count += 1
        s += 1

    elif arr[e] >= x:
        # print('over :', arr[e])
        count += 1
        e -= 1

    elif arr[s] + arr[e] >= x/2:
        # print('sum :', arr[s], '+', arr[e])
        count += 1
        s += 1
        e -= 1

    elif arr[s] + arr[e] < x/2:
        # small_arr.append(arr[s])
        small_count += 1
        s += 1

if s == e:
    if arr[s] >= x:
        count += 1
    else:
        small_count += 1
        # small_arr.append(arr[s])

small_count = small_count // 3

# print('small :', small_arr)
print(count + small_count)

# 1 2
# 2
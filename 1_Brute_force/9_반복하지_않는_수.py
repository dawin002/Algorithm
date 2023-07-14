num = 1
count = 0
arr = []
while count < 1_000_000:
    s_num = str(num)
    if len(s_num) == len(set(s_num)):
        arr.append(num)
        count += 1
        num += 1
    else:
        idx = -1
        for i in range(len(s_num)):
            for j in range(i+1, len(s_num)):
                if s_num[i] == s_num[j]:
                    idx = j
                    break
            if idx != -1:
                break
        pass_size = len(s_num) - idx - 1
        num += 10 ** pass_size

while True:
    i = int(input())
    if i == 0:
        break
    print(arr[i - 1])



# input
# 27
# 29
# 25
# 27
# 10000
# 26057
# 1000000
# 26195083
# 0

# len = 2
# 01
# 11
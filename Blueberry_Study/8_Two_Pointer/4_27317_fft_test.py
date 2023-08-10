import math
import copy
import sys
input = sys.stdin.readline

n, m, k, t = map(int, input().split())
f_times = []
# arr = ['.' for _ in range(m+1)] #################

for _ in range(n):
    x, y = map(int, input().split())
    f_times.append((x, y))
    # for i in range(x, y): #################
    #     arr[i] = '#'

f_times.append((m, m))

head_idx = 0
tail_idx = 0
start = 0
end = 0
k_cnt = 0
maxi = 0

while start < m:

    # arr2 = copy.deepcopy(arr) ###############
    # print(f'k:{k_cnt}  {start} ~ {end}, idx:{head_idx}, {tail_idx}, length:{end - start}')
    # for i in range(start, end):
    #     if arr2[i] == '.':
    #         arr2[i] = 1
    # print(*[a % 10 for a in range(m + 1)])
    # print(*arr2)
    # print()

    # 마법 개수 다 썼을 때
    if k_cnt == k:
        maxi = max(maxi, end - start)
        head_start, head_end = f_times[head_idx]
        # 다음 헤드까지의 거리
        head_dis = head_start - start

        # 헤드쪽에 줄일 칸이 없을 때
        if head_dis == 0:
            head_idx += 1
            start = head_end

        # 헤드쪽에 줄일 칸이 있을 때
        else:
            # print(head_start, start, head_dis)
            if head_dis % t == 0:
                start += t
            elif end < head_start:
                start = head_start - k*t
                end = head_end
                k_cnt = k
            elif head_dis % t != 0:
                start += head_dis % t
                # print('에러발생부분', head_start)
            k_cnt -= 1

    # 마법 개수 남았을 때
    elif k_cnt < k:
        if tail_idx > n:
            break
        next_start, next_end = f_times[tail_idx]
        left_dis = (k - k_cnt) * t

        # 남은 마법 거리가 다음 복슬 시작시간보다 작을때
        if left_dis < next_start - end:
            end += left_dis
            k_cnt = k

        # 남은 마법 거리가 다음 복슬 시작시간에 딱맞거나 여튼 다 써야할 때
        else:
            if left_dis < next_start - end + t:
                k_cnt = k
            else:
                k_cnt += math.ceil((next_start - end) / t)
            end = next_end
            tail_idx += 1

    # print()

print(maxi)



# 2 15 3 2
# 3 4
# 11 15
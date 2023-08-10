# n : 복슬복슬 시간대의 수
# m : 총 시간
# k : 마법 개수
# t : 마법 유지시간
#
# 복슬 시간대에는 마법 종료
# 총 시간 이후에도 마법 종료

# k번 이내로 마법 사용하며 최대한 연속으로 복슬할 수 있는 시간 구하기

import sys
input = sys.stdin.readline

n, m, k, t = map(int, input().split())
f_times = []

for _ in range(n):
    x, y = map(int, input().split())
    f_times.append((x, y))

f_times.append((m, m))

head_idx = 0
tail_idx = 0
start = 0
end = 0
k_cnt = 0
maxi = 0

while start < m:
    print(f'k:{k_cnt}  {start} ~ {end}, idx:{head_idx}, {tail_idx}')

    # 마법 개수 다 썼을 때
    if k_cnt == k:
        maxi = max(maxi, end - start)
        head_start, head_end = f_times[head_idx]
        head_dis = head_start - start

        # 헤드쪽에 줄일 칸이 없을 때
        if head_dis == 0:
            head_idx += 1
            start = head_end

        # 헤드쪽에 줄일 칸이 있을 때
        else:
            if head_dis % t == 0:
                start += t
            elif head_dis % t != 0:
                start += head_dis % t
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
                k_cnt += round((next_start - end) / t + 0.5)
            end = next_end
            tail_idx += 1

print(maxi)


# 1 20 3 2
# 10 13

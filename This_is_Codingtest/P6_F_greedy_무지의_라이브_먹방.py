""" 그리디 : 6. 무지의 먹방 라이브"""

# 회전판의 N개 음식 먹어야함
# 1~N번 음식 번호
# 1번부터 시작, 회전판 번호가 증가하는 순서대로 음식 갖다줌
# 마지막 번호 먹으면 회전판에 의해 1번으로 되돌아옴
# 음식 1초동안 먹고 다음 음식 시작
# 다음 음식 : 아직 남은 음식 중 가장 가까운 음식
# 먹방 시작 K초 후 방송중단, 다시 시작할때 몇번부터 먹어야하는지?

""" my code : 정답은 나오지만 시간 초과 """

def mooji_live___failed1(food_times, k):

    count = 0
    stack = []

    for i in range(len(food_times)):
        stack.append([food_times[i], i])

    stack.sort(reverse=True)

    while stack and k - count >= stack[-1][0] * len(stack):
        min_time = stack[-1][0]
        count += min_time*len(stack)
        for i in range(len(stack)):
            stack[i][0] -= min_time
        while stack and stack[-1][0] == 0:
            stack.pop()

    while stack and k - count >= len(stack):
        min_time = len(stack)
        count += min_time
        for i in range(len(stack)):
            stack[i][0] -= 1
        while stack and stack[-1][0] == 0:
            stack.pop()

    if stack:
        stack.sort(key=lambda x: x[1])
        answer = stack[k - count][1]+1

    else:
        answer = -1

    return answer

""" my code : 틀림, 시간은 줄어듬 """

def mooji_live___failed2(food_times, k):

    count = 0
    stack = []

    for i in range(len(food_times)):
        stack.append([food_times[i], i])

    stack.sort(reverse=True)
    length = len(stack)

    while stack and k >= count:

        if stack[-1][0] * length <= k-count:
            min_time = stack[-1][0]
            count += min_time * length
            while stack:
                stack[-1][0] -= min_time
                if stack[-1][0] == 0:
                    stack.pop()
                    length -= 1
                else:
                    break

        else:
            min_time = stack[-1][0]-1
            while min_time * length > k-count:
                min_time -= 1
            if min_time == 0:
                break
            count += min_time * length
            while stack:
                stack[-1][0] -= min_time
                if stack[-1][0] == 0:
                    stack.pop()
                    length -= 1
                else:
                    break

    if stack:
        stack.sort(key=lambda x: x[1])
        answer = stack[k - count][1]+1
    else:
        answer = -1

    return answer


""" answer code """

def mooji_live_ans(food_times, k):
    import heapq

    # 음식을 다 먹는 시간보다 <= k 라면 -1
    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 빼야되니까 우선순위큐 사용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 큐에 삽입
        heapq.heappush(q, (food_times[i], i+1))

    sum_value = 0   # 먹기 위해 사용한 시간
    previous = 0    # 직전에 다 먹은 음식 시간
    length = len(food_times)   # 남은 음식 개수

    # sum_value + (현재 음식 시간 - 직전 음식 시간) * 현재 음식 개수   와  k  비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1     # 다 먹은 음식 제외
        previous = now  # 이전 음식 시간 재설정

    # 남은 음식 중에서 몇 번째 음식인지 확인해 출력
    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_value) % length][1]

food_times = [2, 2, 2]
k = 5
ans = mooji_live_ans(food_times, k)
print(ans)
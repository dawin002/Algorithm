""" 정렬 문제 : 25. 실패율 """

# 실패율 : 스테이지에 도달했으나 아직 못깬 사람 수 / 스테이지에 도달한 사람
# n : 전체 스테이지 수
# stages : 플레이어가 현재 멈춰있는 스테이지 번호가 담긴 배열

n1 = 5
stages1 = [2, 1, 2, 6, 2, 4, 3, 3]
input1 = (n1, stages1)

n2 = 4
stages2 = [4, 4, 4, 4, 4]
input2 = (n2, stages2)

# 스테이지 5탄까지 있음
# 6은 모두 깬 사람
# 3은 3탄에 머무르는 사람(2탄까지 깸)

""" my code """

def fail_percent(n, stages):
    stage_stay = [0] * (n+2)
    for s in stages:
        stage_stay[s] += 1

    fail = []
    passed = sum(stage_stay)

    for i in range(1, n+1):
        fail.append((i, stage_stay[i]/passed))
        passed -= stage_stay[i]

    print(fail)

    fail.sort(key=lambda x: (-x[1], x[0]))

    answer = [f[0] for f in fail]
    return answer

print(fail_percent(*input1))



""" answer code """

def fail_percent_ans(n, stages):
    answer = []
    length = len(stages)

    for i in range(1, n+1):
        # 해당 스테이지에 머물러있는 사람의 수 계산
        count = stages.count(i)

        # 실패율 계산
        if length == 0:
            fail = 0
        else:
            fail = count / length

        # 리스트에 (스테이지 번호, 실패율) 원소 삽입
        answer.append((i, fail))
        length -= count  # 여기까지 온(통과든 실패든) 플레이어 수 계산

    answer = sorted(answer, key=lambda t: t[1], reverse=True)

    answer = [i[0] for i in answer]

    return answer

print(fail_percent_ans(*input1))
""" 구현 문제 : 14. 외벽 점검 """

# 벽 : 동그란 모양
# 외벽 둘레 : n
# 1시간동안 친구 보내 외벽 점검
# 친구마다 1시간 이동거리 다름
# 외벽 정북 방향 좌표 : 0
# 취약지점 위치 : 정북에서 시계방향으로 떨어진 거리
# 친구 이동 : 어딘가에서 시계/반시계로 이동
#
# 외벽 길이 : n  ( 1 <= n <= 200 )
# 취약지점 위치 배열 : weak  ( 1 <= len(weak) <= 15 , 오름차순, 0 이상 n-1 이하 정수 )
# 각 친구 1시간 이동거리 배열 : dist  ( 1 <= len(dist) <= 8 , 1 이상 100 이하 정수 )
#
# 취약지점 점검하기 위해 보내야하는 친구 최소값 출력

n1 = 12
weak1 = [1, 5, 6, 10]
dist1 = [1, 2, 3, 4]
input1 = [n1, weak1, dist1]

""" my solution """

# 굳이 외벽을 배열로 만들지 않아도 될듯
# -> 외벽 좌표를 (다음 취약 지점까지의 거리)로 나타내도 되지 않을까?

""" answer solution """


# 데이터 개수 적음 -> 완전 탐색 고려
# 원형 데이터 처리 : 길이를 2배로 늘려 원형을 일자로 만듬

def outside_check_ans(n, weak, dist):
    from itertools import permutations

    # 길이를 2배로 늘려 원형 리스트를 일자 리스트로 바꿈
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)

    # 투입할 친구 수의 최소값 초기화
    answer = len(dist) + 1

    # 0부터 length - 1 까지의 위치를 각각 시작점으로 설정하고 가능한지 탐색
    for start_pos in range(length):

        # 친구를 나열하는 모든 경우의 수 각각에 대하여 확인
        for friends in list(permutations(dist, len(dist))):
            count = 1  # 투입한 친구 수

            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start_pos] + friends[count - 1]

            # 시작점부터 모든 취약 지점 확인
            for index in range(start_pos, start_pos + length):

                # 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[index]:
                    count += 1  # 새로운 친구 투입

                    if count > len(dist):  # 더 투입이 불가능하면 종료
                        break

                    position = weak[index] + friends[count - 1]

            answer = min(answer, count)  # 최소값 계산

    if answer > len(dist):
        return -1
    return answer


print(outside_check_ans(*input1))

""" 내가 적은 해설 """

def outside_check_ans2(n, weak, dist):
    from itertools import permutations

    # n : 외벽 둘레
    # weak : 외벽 취약 지점 좌표 리스트
    # dist : 친구당 탐색 거리 리스트

    length = len(weak)  # 취약 지점 개수

    # weak + weak 로 리스트 길이를 2배로 늘려 원형 리스트를 일자 리스트로 바꿈
    for i in range(length):
        weak.append(weak[i] + n)

    # 투입한 친구 수 초기화 : 최소값 찾아야 하므로 전체 친구수 + 1 로 초기화
    answer = len(dist) + 1

    # start_pos : 취약 지점 탐색 시작 위치를 설정할 변수 0 ~ length-1 까지 반복. weak의 인덱스로 사용
    for start_pos in range(length):

        # dist로 만들 수 있는 모든 순열에서 하나씩 꺼내 friends 로 사용 (친구 어떤 순서로 투입할지)
        for friends in list(permutations(dist, len(dist))):
            count = 1  # 지금 투입한 친구 수 (현재는 1인데 한명 투입할때마다 1씩 증가 예정)

            # 현재 투입한 count-1 번째 친구가 어디까지 탐색할 수 있는지
            position = weak[start_pos] + friends[count - 1]

            # index : weak의 이번 탐색의 시작지점인 start_pos 번째 요소부터 취약지점 개수 만큼 증가하며 반복
            for index in range(start_pos, start_pos + length):

                # 지금 친구가 index 번째 취약 지점을 점검할 수 없는 경우
                # position (현재 투입한 친구가 탐색할 수 있는 마지막 위치) < weak[index] (다음 취약 지점)
                if position < weak[index]:
                    count += 1  # 새로운 친구 투입

                    if count > len(dist):  # 더 투입이 불가능하면 종료
                        break

                    # 새로 투입된 친구가 탐색할 수 있는 마지막 위치 갱신
                    position = weak[index] + friends[count - 1]

            answer = min(answer, count)  # 최소값 계산

    if answer > len(dist):
        return -1
    return answer
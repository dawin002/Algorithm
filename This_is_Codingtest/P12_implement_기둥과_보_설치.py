""" 구현 문제 : 기둥과 보 설치 """

""" my code """

""" 처음에 문제 푸는 방식 몰랐었음, 해설보고 성공 """

n1 = 5
build_frame1 = [[1, 0, 0, 1],
               [1, 1, 1, 1],
               [2, 1, 0, 1],
               [2, 2, 1, 1],
               [5, 0, 0, 1],
               [5, 1, 0, 1],
               [4, 2, 1, 1],
               [3, 2, 1, 1]]

n2 = 5
build_frame2 = [[0, 0, 0, 1],
                [2, 0, 0, 1],
                [4, 0, 0, 1],
                [0, 1, 1, 1],
                [1, 1, 1, 1],
                [2, 1, 1, 1],
                [3, 1, 1, 1],
                [2, 0, 0, 0],
                [1, 1, 1, 0],
                [2, 2, 0, 1]]

def check_possible(n, fList):
    for tmp in fList:
        x, y, type = tmp
        # 기둥일 때
        if type == 0:
            if y == 0 or (x-1, y, 1) in fList or (x, y, 1) in fList or (x, y-1, 0) in fList:
                continue
            return False
        # 보일 때
        else:
            if (x, y-1, 0) in fList or (x+1, y-1, 0) in fList or (x-1, y, 1) in fList and (x+1, y, 1) in fList:
                continue  # A==0 or B==0 or ( C==0 and D==0 ) --> 여기 ( ) 벗겨도 연산자 우선순위 and > or 이어서 괜찮음
            return False
    return True

def build_frame_and_bo(n, build_frame):
    now_list = set()
    for frame in build_frame:
        x, y, type, operate = frame
        if operate == 1:
            now_list.add((x, y, type))
            if not check_possible(n, now_list):
                now_list.remove((x, y, type))
        else:
            now_list.remove((x, y, type))
            if not check_possible(n, now_list):
                now_list.add((x, y, type))

    result = list(map(list, now_list))
    return sorted(result, key=lambda x: (x[0], x[1], x[2]))

result = build_frame_and_bo(n1, build_frame1)
print(result)

result = build_frame_and_bo(n2, build_frame2)
print(result)
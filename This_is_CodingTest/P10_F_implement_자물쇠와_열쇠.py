""" 구현 문제 : 10. 자물쇠와 열쇠 """

""" my code """

""" 풀이 시간 초과해서 나중에 다시 풀어보기 + 2차원 배열 회전 함수 구현 실패 """

key = [[0, 0, 0],
       [1, 0, 0],
       [0, 1, 1]]

lock = [[1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]]

def lockAndKey(key, lock):
    import copy

    # 2차원 리스트 시계방향 90도 회전 함수
    def rotate_matrix_by_90_degree(arr):
        n = len(key)
        m = len(key[0])
        result = [[0] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                result[j][n-i-1] = arr[i][j]
        return result

    # 열쇠 꽂기 함수
    def input_key(tmp_map, key, i_map, j_map):
        # lock 을 복사한 tmp_map 에 key 합치기
        for i_key in range(n):
            for j_key in range(n):
                tmp_map[i_map + i_key][j_map + j_key] += key[i_key][j_key]

    # 열쇠 맞는지 확인하는 함수
    def check_key(tmp_map, n):
        # 합친 tmp_map 의 lock 부분에 1이 아닌 숫자 있는지 확인하기
        lock_range = range(n-1, 2*n-1)
        for i_lock in lock_range:
            for j_lock in lock_range:
                if tmp_map[i_lock][j_lock] != 1:
                    return False
        return True

    # 확인용으로 만든 전체 2차원 리스트 출력 함수
    def print_lock_map(arr, rot, i_map, j_map, found_key):
        print('lock map')
        print(f'rot={rot}, i_m={i_map}, j_m={j_map}')
        for a in arr:
            print(a)
        print(f'found_key={found_key}')
        print()

    n = len(lock)

    # lock 주위를 n-1만큼씩 0으로 감싼 (key 맞춰볼) lock_map 만들기
    lock_map = [[0]*(n*3-2) for _ in range(n*3-2)]
    for i in range(n):
        for j in range(n):
            lock_map[i+n-1][j+n-1] = lock[i][j]

    # 4방향 회전시키며 진행
    for rot in range(4):
        # key 90도 회전
        key = rotate_matrix_by_90_degree(key)
        # " key = " 꼭 붙여야함! 이유는 key 가 외부에서 들어온 매개변수이기 때문에 원본이 안바뀜

        # tmp_map 의 (0,0) 부터 열쇠 한 칸씩 이동하며 꽂아보기
        for i_map in range(2*n-1):
            for j_map in range(2*n-1):
                # 원본인 lock_map 을 복제한 tmp_map 생성
                tmp_map = copy.deepcopy(lock_map)
                # 열쇠 꽂기 (tmp_map 과 key 합침)
                input_key(tmp_map, key, i_map, j_map)
                # 열쇠 확인 (tmp_map 의 lock 부분에 1이 아닌 원소 있는지 확인)
                found_key = check_key(tmp_map, n)
                # 맞는 열쇠 찾으면 바로 True 반환
                print_lock_map(tmp_map, rot, i_map, j_map, found_key)
                if found_key:
                    return True
    # 끝까지 맞는 열쇠 못 찾았기 때문에 True 반환
    return False

print('answer :', lockAndKey(key, lock))



""" answer code """

# 내 코드랑 다른 점
# 1. lock 을 넣는 배경 크기를 n*3 x n*3 으로 설정 -> 코드 단순화
#    내 코드는 n*3-2 x n*3-2
# 2. key 넣고 맞는지 확인하고 키 다시 뺌
#    내 코드는 lock_map 복제한 tmp_map 만들어서 넣고 확인하고 tmp_map 버림

def lockAndKey_ans(key, lock):

    # 2차원 리스트 시계방향 90도 회전 함수
    def rotate_matrix_by_90_degree(arr):
        n = len(arr)
        m = len(arr[0])
        result = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                result[j][n-i-1] = arr[i][j]
        return result

    # 자물쇠의 중간 부분이 모두 1인지 확인
    def check(new_lock):
        lock_length = len(new_lock)//3
        for i in range(lock_length, lock_length*2):
            for j in range(lock_length, lock_length*2):
                if new_lock[i][j] != 1:
                    return False
        return True

    len_lock = len(lock)
    len_key = len(key)

    # 자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0] * (len_lock * 3) for _ in range(len_lock * 3)]

    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(len_lock):
        for j in range(len_lock):
            new_lock[i + len_lock][j + len_lock] = lock[i][j]

    # 4가지 방향에 대해서 확인
    for rotation in range(4):
        key = rotate_matrix_by_90_degree(key)
        for x in range(len_lock * 2):
            for y in range(len_lock * 2):
                # 자물쇠에 열쇠를 끼워 넣기
                for i in range(len_key):
                    for j in range(len_key):
                        new_lock[x+i][y+i] += key[i][j]
                # 새로운 자물쇠에 열쇠가 맞는지 검사
                if check(new_lock) == True:
                    return True
                # 자물쇠에서 열쇠를 다시 빼기
                for i in range(len_key):
                    for j in range(len_key):
                        new_lock[x + i][y + i] -= key[i][j]
    return False

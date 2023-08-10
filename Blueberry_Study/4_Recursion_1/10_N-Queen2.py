n = int(input())
arr_j = []
count = 0

def recur(queen, now_i):
    if queen == n:
        global count
        count += 1
        return

    i = now_i  # 어차피 모든 줄에 하나의 퀸이 있어야하므로 몇번 줄에 넣을지는 고민 x
    for j in range(n):
        if j in arr_j:
            continue
        for pre_i in range(len(arr_j)):
            if pre_i - arr_j[pre_i] == i - j:
                break
            if pre_i + arr_j[pre_i] == i + j:
                break
        else:
            arr_j.append(j)
            recur(queen + 1, i+1)  # 재귀 들어가기
            arr_j.pop()

recur(0, 0)  # recur( 현재 발견된 퀸 수 , 탐색할 i 값 )

print(count)
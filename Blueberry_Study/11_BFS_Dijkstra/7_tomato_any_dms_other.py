import sys
def input(): return sys.stdin.readline().rstrip("\r\n")

shape = list(map(int, input().split()))
move = [1]

for i in shape:
    move.append(move[-1] * i)

board = [i for _ in range(move[-1] // shape[0]) for i in list(map(int, input().split()))]

tomato_cnt = board.count(0)

q1, q2 = [], [i for i in range(len(board)) if board[i] == 1]

ans = 0

while q2:
    q1, q2 = q2, []
    for cur in q1:
        for i in range(len(move) - 1):
            if (cur - move[i]) // move[i + 1] == cur // move[i + 1] and board[cur - move[i]] == 0:
                q2.append(cur - move[i])
                board[cur - move[i]] = 1
            if (cur + move[i]) // move[i + 1] == cur // move[i + 1] and board[cur + move[i]] == 0:
                q2.append(cur + move[i])
                board[cur + move[i]] = 1
    if q2:
        ans += 1
        tomato_cnt -= len(q2)

if tomato_cnt > 0:
    print(-1)
else:
    print(ans)
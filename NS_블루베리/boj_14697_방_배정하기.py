""" 14697 - 방 배정하기 """

# 3 종류의 방 (침대 수 다름)
# 3 타입 방의 침대 수 A, B, C, 학생 수 N 주어짐
# 1 <= A < B < C <= 50 , 1 <= N <= 300
# 모든 학생이 남는 침대 없이 들어갈 수 있으면 1, 아니면 0 출력
# (특정 방 종류 안써도 됨)

""" my solution """

def students_in_room():
    a, b, c, n = map(int, input().split())
    ans = 0
    for i in range(0, n//c+1):
        for j in range(0, (n-c*i)//b+1):
            ra, rb, rc = a*((n - (c*i + b*j)) // a), b*j, c*i
            s = ra + rb + rc
            if (n - (c*i + b*j)) % a == 0:
                ans = 1
                break
        if ans == 1:
            break
    print(ans)
students_in_room()
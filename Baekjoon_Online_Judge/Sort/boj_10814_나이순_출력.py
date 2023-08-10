""" 10814 : 나이순 출력 """

# 가입순으로 입력됨
# 나이 오름차순, 같으면 가입일 오름차순으로 출력

""" my solution """

def age_first():
    import sys
    input = sys.stdin.readline
    n = int(input())
    arr = []
    for i in range(n):
        age, name = input().split()
        arr.append((int(age), name, i))

    arr.sort(key=lambda x: (x[0], x[2]))
    for a in arr:
        print(a[0], a[1])

# age_first()

""" my solution 2 : 생각해보니까 번호 안매겨도 이미 가입일 순 정렬돼있음 """

def age_first_2():
    import sys
    input = sys.stdin.readline
    n = int(input())
    arr = [list(input().split()) for _ in range(n)]
    arr.sort(key=lambda x: int(x[0]))
    for i in range(n):
        arr[i] = ' '.join(arr[i])
    print('\n'.join(arr))

age_first_2()


""" answer solution : readlines() 사용 """

def age_first_ans():
    import sys
    arr = sys.stdin.readlines()[1:]
    arr.sort(key=lambda x: int(x.split()[0]))
    print("".join(arr))

# age_first_ans()
""" 1225 : 암호생성기 """

# 배열에 8개의 수 있음
# 1 싸이클 : 5단계
# 각 싸이클 : 맨앞 1 감소 후 맨뒤로, 맨앞 2 감소 후 맨뒤로, ... 5 감소 후 맨뒤로 까지
# 맨앞을 줄이자 0 이하가 되면 0으로 바꾼 후 맨뒤로, 암호 만들기 종료.

""" my solution """

def pw_maker():
    t = input()
    arr = list(map(int, input().split()))

    idx = 0
    count_5 = 0
    while True:
        print(arr)
        arr[idx % 8] -= count_5 % 5 + 1
        if arr[idx % 8] <= 0:
            arr[idx % 8] = 0
            break
        idx += 1
        count_5 += 1

    while arr[-1] != 0:
        arr.append(arr.pop(0))

    print(f"#{t}", *arr)

pw_maker()


def pw_maker():
    t = input()
    arr = list(map(int, input().split()))

    count_5 = 0
    while True:
        print(arr)
        a = arr.pop(0)
        a -= count_5 % 5 + 1
        count_5 += 1
        if a <= 0:
            a = 0
            arr.append(a)
            break
        arr.append(a)

    print(f"#{t}", *arr)

pw_maker()


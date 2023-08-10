""" 그래프 이론 문제 : 42. 탑승구 """

# 1~G 번 탑승구 (G개)
# 비행기 P개 도착
# 도착한 비행기 탐승구 중 하나와 1대1 매칭
# 비행기마다 번호 g : 1~g 번 탑승구 중 하나에 매칭 가능
# 매칭 불가능해지면 스톱
# 매칭 가능한 비행기 최대 대수 출력

""" my solution : 실패(시간복잡도 너무 높음) : 그래프로는 못 풀겠음 (결과는 맞음)"""

def plain_docking():
    g = int(input())
    gate = [1] * (g+1)
    gate[0] = 0
    p = int(input())
    count = 0
    for _ in range(p):
        max_gate = int(input())
        for m in range(max_gate, 0, -1):
            if gate[m] == 1:
                gate[m] = 0
                count += 1
                break
        else:
            break

    print(count)

plain_docking()


""" answer solution : 그래프 사용 (서로소 집합 알고리즘) """

""" 
이 코드에서 시간복잡도 낮은 이유 : 
경로 압축 기법 사용해 parent에 루트를 저장하는 방식으로 빈 탑승구 찾아가는 시간복잡도 O(N)로 줄임 
반면, 내 코드는 최악의 경우 빈 탑승구를 찾아 루트까지 N번 반복문을 수행해야해서 시간복잡도 O(N^2)
"""

# 나랑 거의 똑같은 풀이 방식이지만,
# 난 전체 탑승구를 하나의 리스트로 구현, 도킹할 수 있는 가장 큰 번호의 탑승구를 -1 처리
# 책은 전체 탑승구를 그래프로 구현, 도킹할 수 있는 가장 큰 번호의 탑승구를 바로 앞 탑승구와 union() 처리

def plain_docking_ans():

    def find_parent(parent, x):
        if parent[x] == x:
            return x
        parent[x] = find_parent(parent, parent[x])
        return parent[x]

    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    g = int(input())
    p = int(input())

    parent = [0] * (g+1)
    for i in range(1, g+1):
        parent[i] = i

    result = 0
    for _ in range(p):
        data = find_parent(parent, int(input()))
        if data == 0:
            break
        union_parent(parent, data, data-1)
        result += 1

    print(result)

# plain_docking_ans()

# 4
# 3
# 4
# 1
# 1


# 4
# 6
# 2
# 2
# 3
# 3
# 4
# 4

def make_input_max():
    print(50000)
    print(50000)
    for i in range(50000):
        print(50000)

# make_input_max()
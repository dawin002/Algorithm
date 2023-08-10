""" 1240 : 단순 2진 암호코드 """

# 암호코드 8개 숫자
# 올바르면 홀수자리합 * 3 + 짝수자리합 이 10의 배수
# 암호 올바른지 판단하는 스캐너 구현
# 스캐너 : 암호코드 1개가 포함된 직사각형 배열 읽음
# 직사각형 배열은 1, 0으로만 이루어져 있음, 암호코드 제외 부분 0으로 채워짐
# 암호코드에서 숫자 하나는 7개의 비트로 암호화

""" my solution : 더 짧게 구현 가능 """


def my_solution():
    code = ['0001101', '0011001', '0010011', '0111101', '0100011',
            '0110001', '0101111', '0111011', '0110111', '0001011']

    def read_code():
        global code
        n, m = map(int, input().split())
        arr = []
        for i in range(n):
            line = input()
            if '1' in line:
                s = line

        end = m - 1 - s[::-1].find('1')
        start = end - 55
        s = s[start:end + 1]

        for i in range(8):
            word = s[i * 7:(i + 1) * 7]
            arr.append(code.index(word))

        res = 0
        for i in range(8):
            if i % 2 == 0:
                res += arr[i] * 3
            else:
                res += arr[i]

        if res % 10 == 0:
            return sum(arr)
        else:
            return 0

    T = int(input())
    for test_case in range(1, T + 1):
        print(f"#{test_case} {read_code()}")


""" shorter solution """


def short_solution():
    T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    for t in range(1, T + 1):
        d = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6,
             '0111011': 7, '0110111': 8, '0001011': 9}
        N, M = map(int, input().split())
        b = ''
        for _ in range(N):
            a = input()
            if '1' in a:
                a = a[a.rindex('1') - 55:a.rindex('1') + 1]
                b = [a[i * 7:(i + 1) * 7] for i in range(8)]
        u = v = c = 0
        for i in range(8):
            if i % 2 < 1:
                u += d[b[i]]
            else:
                v += d[b[i]]
        c = u + v
        u = u * 3 + v
        print(f'#{t}', c if u % 10 < 1 else 0)

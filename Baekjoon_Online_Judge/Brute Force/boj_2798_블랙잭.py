""" 2798 : 블랙잭 """

# 규칙 : 카드 합 21 넘지 않는 최대값
# 각 카드 양의 정수 쓰여있음
# 숫자 카드 n 장 공개
# 숫자 m 으로 블랙잭
# 3장으로 만들 수 있는 최대값 출력

""" my solution : 느림 (combinations 믿고 브루트포스 미적용) """

"""
    브루트 포스 문제라 쓸모 없는 가지를 빨리 쳐내는게 중요한데
    1번 솔루션은 모든 경우의 조합을 combinations로 확인한 반면
    2번 솔루션은 반복문 도중 적당한 때에 continue로 끊어줘서 오히려 빠름
    라이브러리 함수보다 반복문이 더 빠를 때도 있다! 브루트 포스 에서는
"""

def black_jack():
    import sys
    from itertools import combinations
    input = sys.stdin.readline
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    card_set = set(combinations(arr, 3))
    max_set = set([sum(s) for s in card_set if sum(s) <= m])
    print(max(max_set))
black_jack()

""" my solution 2 : faster (브루트포스 적용) """

def black_jack_2():
    import sys
    input = sys.stdin.readline
    n, m = map(int, input().split())
    card = sorted(list(map(int, input().split())), reverse=True)
    max_card = 0
    for a in range(0, len(card)-2):
        if card[a] > m:
            continue
        for b in range(a+1, len(card)-1):
            if card[a] + card[b] > m:
                continue
            for c in range(b+1, len(card)):
                sum_card = card[a] + card[b] + card[c]
                if max_card <= sum_card <= m:
                        max_card = sum_card

    print(max_card)

black_jack_2()
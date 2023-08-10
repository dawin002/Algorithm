
""" 구현 문제 : 7. 럭키 스트레이트 """

""" my code """

def luckyStraight():
    n = list(map(int, input()))
    half = len(n)//2
    if sum(n[:half]) == sum(n[half:]):
        print('LUCKY')
    else:
        print('READY')
luckyStraight()
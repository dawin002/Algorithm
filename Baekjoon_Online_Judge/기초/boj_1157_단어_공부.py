""" 1157 : 단어 공부 """

# 입력된 문자열에서 가장 많이 사용된 알파벳 출력
# 가장 많이 사용된 알파벳 하나 이상일 경우 ? 출력

""" my solution """
# 문자열을 모두 대문자로 바꿔서 계산해야 편함

import sys
input = sys.stdin.readline

arr = [0] * 26
st = input().rstrip().upper()
for s in st:
    arr[(ord(s)-65)] += 1
m = max(arr)
if arr.count(m) > 1:
    print('?')
else:
    print(chr(arr.index(m)+65))
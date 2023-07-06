""" 21275 : 폰 호석만 """

st = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] + [chr(j) for j in range(ord('a'), ord('z')+1)]

# xa, xb = input().split()

xa, xb = '11', 'jh'

for a in range(1, 36):
    idx_xa = 0
    x1 = 0
    for i in list(xa)[::-1]:
        x1 += a ** idx_xa * st.index(i)
        print(x1)
    # for b in range(1, 36):


print(36 * 36)
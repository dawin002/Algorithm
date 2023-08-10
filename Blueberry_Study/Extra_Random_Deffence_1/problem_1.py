""" 21275 : 폰 호석만 """

st = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] + [chr(j) for j in range(ord('a'), ord('z')+1)]

xa, xb = input().split()

# xa, xb = '11', 'jh'
answer = []

for a in range(1, 36):
    idx_xa = 0
    x1 = 0
    for i in list(xa)[::-1]:
        x1 += a ** idx_xa * st.index(i)
        idx_xa += 1

        for b in range(1, 36):
            if a == b:
                continue
            x2 = 0
            idx_xb = 0
            for j in list(xb)[::-1]:
                x2 += b ** idx_xb * st.index(j)
                idx_xb += 1

            if x1 == x2:
                answer.append(x1)
                print(x1, a, b)
                if len(answer) > 1:
                    break
        if len(answer) > 1:
            break

if len(answer) > 1:
    print("Multiple")
elif len(answer) == 0:
    print("Impossible")
else:
    print(*answer)
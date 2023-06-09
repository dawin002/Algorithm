# n = int(input())
n = 4
arr = []
count = 0

def recur():
    found = False
    for i in range(n):
        for j in range(n):
            if not arr:
                arr.append((i, j))
                recur()
                arr.pop()
            else:
                for qi, qj in arr:
                    if qi == i:
                        continue
                    if qj == j:
                        continue
                    if qi - qj == i - j:
                        continue
                    if qi + qj == i + j:
                        continue
                    print(i, j)
                    found = True
                    arr.append((i, j))
                    recur()
                    arr.pop()
    if not found:
        global count
        count += 1
        return


recur()

print(count)
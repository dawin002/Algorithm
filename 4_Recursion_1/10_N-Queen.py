n = int(input())
# n = 11
arr = []
count = 0

# usable_j = set([i for i in range(n)])
# used_j = set([16])

# def print_m():
#     mmap = [['.' for _ in range(n)] for _ in range(n)]
#     for x, y in arr:
#         mmap[x][y] = 'Q'
#     print()
#     for line in mmap:
#         print(*line)
#     print()

def recur(queen, prei, prej):
    if queen == n:
        global count
        count += 1
        # print_m()
        return

    for i in range(prei, n):
        # for j in usable_j:
        for j in range(n):
            # if j not in used_j:
                for qi, qj in arr:
                    if qi == i:
                        break
                    if qj == j:
                        break
                    if qi - qj == i - j:
                        break
                    if qi + qj == i + j:
                        break
                else:
                    arr.append((i, j))
                    # usable_j.remove(j)
                    # used_j.add(j)
                    recur(queen+1, i, j)
                    arr.pop()
                    # usable_j.add(j)
                    # used_j.remove(j)

# for i in range(n):
i = 0
for j in range(n):
    arr.append((i, j))
    # usable_j.remove(j)
    # used_j.add(j)
    recur(1, i, j)
    arr.pop()
    # used_j.remove(j)
    # usable_j.add(j)

print(count)
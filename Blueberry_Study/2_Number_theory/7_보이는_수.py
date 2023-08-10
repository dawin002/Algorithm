# n   : 1   2   3   4   5   6   7
# ans : 3   5   9   13  21  27  39
# cha :   2   4   4   8   6   12

tc = int(input())
for _ in range(tc):
    n = int(input())
    i = 1
    ans = 3
    x = 2
    while i < n:
        if i % 2 == 1:
            ans += x
        if i % 2 == 0:
            ans += x*2
            x += 2
        i += 1

    print(ans)
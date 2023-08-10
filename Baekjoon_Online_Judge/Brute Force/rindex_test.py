
""" rindex() 테스트 """

a = '0000011101101100010111011011000101100010001101001001101110110000000000'
m = len(a)

end1 = m - a[::-1].index('1')
sta1 = end1 - 56
print(sta1, end1, end1-sta1)
print(len(a[sta1:end1]))
print(a[sta1:end1])

end2 = a.rindex('1') + 1
sta2 = end2 - 56
print(sta2, end2, end2-sta2)
print(len(a[sta2:end2]))
print(a[sta2:end2])



data = [
    "CBBCBAAB",
    "CCCBABCB",
    "CAAAACAB",
    "BACCCCAC",
    "AABCBBAC",
    "ACAACABC",
    "BCCBAABC",
    "ABBBCCAA"
    ]
T, i, j = 4, 3, 0
print([line[j] for line in data[i:i+T]])


arr2 = [(1, 2), (3, 4), (5, 6)]

for a in arr2:
    x, y = a
    print(x, y)

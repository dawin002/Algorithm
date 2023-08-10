PRE_ = 0
IN_ = 1
POST_ = 2

def recur(node, order):
    if node == ord('.'):
        return

    if order == PRE_:
        print(chr(node), end='')

    recur(tree[node][0], order)

    if order == IN_:
        print(chr(node), end='')

    recur(tree[node][1], order)

    if order == POST_:
        print(chr(node), end='')

n = int(input())

# A는 아스키코드로 65니까
# 배열을 충분히 크게 만들고
# A의 자식들을 65번째 인덱스에 넣어주기

tree = [[] for _ in range(128)]

# 문자열로 받는 것보다 숫자로 받는게 좋은점도 있음
for _ in range(n):
    # 아스키코드로 변환할 것 (숫자로 변환 ord, 문자로 변환 chr)
    node, left, right = map(ord, input().split())
    # 처음부터 아스키로는 못하고 string으로 받은후에 변환하는 방법밖에 없나요???

    tree[node].append(left)
    tree[node].append(right)

recur(ord('A'), PRE_)
print()
recur(ord('A'), IN_)
print()
recur(ord('A'), POST_)


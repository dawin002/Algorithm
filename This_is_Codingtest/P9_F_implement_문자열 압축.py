""" 구현 문제 : 9. 문자열 압축 """

""" 틀린건 아닌데 풀이 시간을 초과해서 다시 풀어볼 것 """

""" my code """

def zipString():
    strs = input()
    minLen = len(strs)

    for zipLen in range(1, len(strs) // 2 + 1):
        tmpLen = len(strs)
        prepre = ''
        pre = strs[:zipLen]

        for i in range(1, len(strs) // zipLen):
            now = strs[i * zipLen:(i + 1) * zipLen]
            if prepre != pre == now:
                tmpLen -= zipLen - 1
            elif prepre == pre == now:
                tmpLen -= zipLen
            prepre = pre
            pre = now

        minLen = min(minLen, tmpLen)

    print(minLen)


""" answer code """

def zipStr_ans():
    s = input()
    answer = len(s)

    for step in range(1, len(s)//2+1):
        compressed = ""
        prev = s[0:step]
        count = 1

        for j in range(step, len(s), step):
            # 이전값, 현재값  비교, 같으면 :
            if prev == s[j:j+step]:
                count += 1  # 카운트 ++
            # 다르면 :
            else:
                # 카운트 2 이상이면: prev 앞에 카운트 붙여서 압축문자열에 이어붙임
                # 2 이상 아니면:  압축문자열에 prev만 이어붙임
                compressed += str(count) + prev if count >= 2 else prev

                prev = s[j:j+step]  # 현재값으로 이전값 설정
                count = 1           # 카운트 1로 되돌림

        # 남아 있는 문자열 처리
        compressed += str(count) + prev if count >= 2 else prev
        # 만들어지는 압축 문자열 중 가장 짧은게 정답
        answer = min(answer, len(compressed))

    print(answer)

""" my code (과정 출력)"""

def zipStr_test():
    strs = 'xababcdcdababcdcd'
    minLen = len(strs)
    print(f'minLen={minLen}')
    for zipLen in range(1, len(strs)//2+1):
        print('==============================')
        tmpLen = len(strs)
        print('zipLen =', zipLen)
        prepre = ''
        pre = strs[:zipLen]
        for i in range(1, len(strs)//zipLen):
            now = strs[i*zipLen:(i+1)*zipLen]
            print(f'i={i}, ppre={prepre}, pre={pre}, now={now}')
            if prepre != pre == now:
                tmpLen -= zipLen - 1
            elif prepre == pre == now:
                tmpLen -= zipLen
            prepre = pre
            pre = now
            print(f'tmpLen={tmpLen}')
        minLen = min(minLen, tmpLen)
        print(f'tmpLen={tmpLen} --> minLen={minLen}')
    print(minLen)

# zipStr_test()
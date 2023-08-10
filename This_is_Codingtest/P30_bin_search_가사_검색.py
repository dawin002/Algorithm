""" 이진 탐색 문제 : 30. 가사 검색 """

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

""" my solution : 맞았음, 하지만 조금 더 개선할 부분 존재 """

# 1. 모든 단어를 길이로 나누어 저정해두면 words 전체를 탐색하며 keyword 와 길이가 같은 word 만
#    골라내는 작업 한 번만 수행할 수 있음
#
# 2. keyword 가 ? 로 시작하는 경우 keyword 와 words 의 모든 word 를 reverse 해야 하므로
#    reverse 된 word 의 길이별 리스트 또한 만들어 둬야 함
#
# 3. 문자열 뒤집기 쉬운 방법 있는데 어렵게 함
#    내 방법 : word = ''.join(reversed(list(word)))
#    책 방법 : word = word[::-1]
#
# 4. keyword 와 word 를 비교할 때 '?'를 제거하는 방식
#    내 방법 : '?'를 제외한 유효한 부분만 슬라이싱한 새로운 keyword 와 words 리스트 생성
#    책 방법 : keyword의 ?를 다른 문자로 치환
#            bisect_left(keyword).replace('?', 'a') : 'a' 해야 가장 왼쪽 인덱스 반환
#            bisect_right(keyword).replace('?', 'z') : 'z' 해야 가장 왼쪽 인덱스 반환

def song_search(words, queries):
    from bisect import bisect_left, bisect_right
    result_list = []
    for keyword in queries:
        result = 0
        length = len(keyword)
        len_useful_k = 0
        for k in keyword:
            if k != '?':
                len_useful_k += 1
        new_words = []
        if keyword[0] == keyword[-1] == '?':
            for w in words:
                if len(w) == length:
                    result += 1
        else:
            if keyword[0] == '?':
                keyword = ''.join(reversed(list(keyword)))
                for i in range(len(words)):
                    if len(words[i]) == length:
                        new_words.append(''.join(reversed(list(words[i])))[0:len_useful_k])
            else:
                for i in range(len(words)):
                    if len(words[i]) == length:
                        new_words.append(words[i][0:len_useful_k])

            keyword = keyword[0:len_useful_k]
            new_words.sort()

            idx_left = bisect_left(new_words, keyword)
            idx_right = bisect_right(new_words, keyword)
            result = idx_right - idx_left

        result_list.append(result)

    return result_list

# print(song_search(words, queries))


""" answer solution """

def song_search_ans(words, queries):
    from bisect import bisect_left, bisect_right

    def count_by_range(arr, left, right):
        left_idx = bisect_left(arr, left)
        right_idx = bisect_right(arr, right)
        return right_idx - left_idx

    # 모든 단어를 길이마다 나누어 저장한 리스트
    arr = [[] for _ in range(10001)]
    # 모든 단어를 뒤집어서 길이마다 나누어 저장한 리스트
    re_arr = [[] for _ in range(10001)]

    answer = []

    # 모든 단어와 뒤집어진 단어 길이에 맞게 리스트에 저장
    for word in words:
        arr[len(word)].append(word)
        re_arr[len(word)].append(word[::-1])

    for i in range(10001):
        arr[i].sort()
        re_arr[i].sort()

    for q in queries:
        if q[0] != '?':
            res = count_by_range(arr[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else:
            res = count_by_range(re_arr[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        answer.append(res)

    return answer

# print(song_search_ans(words, queries))
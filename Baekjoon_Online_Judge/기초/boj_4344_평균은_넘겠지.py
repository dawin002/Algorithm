""" 4344 : 평균은 넘겠지 """

# 각 테스트케이스의
# 학생수, 각 학생의 점수 입력
# 평균 점수보다 높은 학생 비율 소수점 3자리까지 반올림해서 출력

""" my solution """

for _ in range(int(input())):
    n, *arr = map(int, input().split())
    avg = sum(arr)/n
    per = len([a for a in arr if a > avg])/n*100
    print(f"{per:.3f}%")
""" 일반적인 프로그래밍 언어와 다른 문법 - if 문 """
""" 6065 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝수만 출력하기 """

# 3개의 정수(a, b, c)가 입력되었을 때, 짝수만 출력해보자.

# 참고
# if 조건식 :
#   실행1  # 조건식의 평가값이 True인 경우 들여쓰기를 이용해 순서대로 명령 작성한다.
#   실행2
# 실행3  # 들여쓰기를 하지 않은 부분은 조건식에 상관이 없음

# python 에서는 논리적 실행단위인 코드블록(code block)을 표현하기 위해 들여쓰기를 사용한다.
# 들여쓰기 방법은 탭(tab), 공백(space) 4개 등 여러 가지 방법을 사용할 수 있지만
# 한 소스코드 내에서 들여쓰기 길이와 방법은 똑같아야 한다.

# a, b, c = input().split(' ')
# if(int(a)%2==0) :
#   print(int(a))
# if(int(b)%2==0) :
#   print(int(b))
# if(int(c)%2==0) :
#   print(int(c))

#
#
#
#
""" 일반적인 프로그래밍 언어와 다른 문법 - if 문 """
""" 6066 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝/홀 출력하기 """

# 3개의 정수(a, b, c)가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.

# a, b, c = input().split(' ')

# if int(a)%2==0 :
#   print("even")
# else :
#   print("odd")

# if int(b)%2==0 :
#   print("even")
# else :
#   print("odd")

# if int(c)%2==0 :
#   print("even")
# else :
#   print("odd")

#
#
#
#
""" 6067 : [기초-조건/선택실행구조] 정수 1개 입력받아 분류하기 """

# 0이 아닌 정수 1개가 입력되었을 때,
# 음(-)/양(+)과 짝(even)/홀(odd)을 구분해 분류해보자.
# 음수이면서 짝수이면, A
# 음수이면서 홀수이면, B
# 양수이면서 짝수이면, C
# 양수이면서 홀수이면, D
# 를 출력한다.

# a = int(input())
# if a<0 :
#   if a%2==0 :
#     print('A')
#   else :
#     print('B')
# else :
#   if a%2==0 :
#     print('C')
#   else :
#     print('D')

#
#
#
#
""" 일반적인 프로그래밍 언어와 다른 문법 : if - elif 문 """
""" 6068 : [기초-조건/선택실행구조] 점수 입력받아 평가 출력하기 """

# 점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.

# 평가 기준
# 점수 범위 : 평가
#  90 ~ 100 : A
#  70 ~  89 : B
#  40 ~  69 : C
#   0 ~  39 : D
# 로 평가되어야 한다.

# a = int(input())
# if a<=100 and a>=90 :
#   print('A')
# elif a >= 70 :
#   print('B')
# elif a >= 40 :
#   print('C')
# elif a >= 0 :
#   print('D')
# else :
#   print("ERROR")

#
#
#
#
""" 6069 : [기초-조건/선택실행구조] 평가 입력받아 다르게 출력하기 """

# 평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.

# 평가 내용

# A : best!!!
# B : good!!
# C : run!
# D : slowly~
# 나머지 문자들 : what?

# c = input()
# if c=='A' :
#   print("best!!!")
# elif c=='B' :
#   print("good!!")
# elif c=="C" :
#   print("run!")
# elif c=="D" :
#   print("slowly~")
# else :
#   print("what?")

#
#
#
#
""" 6070 : [기초-조건/선택실행구조] 월 입력받아 계절 출력하기 """

# 월이 입력될 때 계절 이름이 출력되도록 해보자.

# 월 : 계절 이름
# 12, 1, 2 : winter
#  3, 4, 5 : spring
#  6, 7, 8 : summer
#  9, 10, 11 : fall

# m = int(input())
# n = m//3
# if n==1 :
#   month = 'spring'
# elif n==2 :
#   month = 'summer'
# elif n==3 :
#   month = 'fall'
# else :
#   month = 'winter'
# print(month)

#
#
#
#

### 6009 : [기초-입출력] 문자 1개 입력받아 그대로 출력하기(설명)(py)

# 문자(character)는 0~9, a~z, A~Z, !, @, #, {, [, <, ... 과 같이 길이가 1인 기호라고 할 수 있다.

# 변수에 문자 1개를 저장한 후 변수에 저장되어 있는 문자를 그대로 출력해보자.

# 참고
# input() 을 사용하면 키보드로 입력한 값을 가져온다.
# 변수 = input()
# 를 실행시키면 키보드로 입력한 값을 왼쪽의 변수에 저장한다.

# 변수(variable)는 어떤 값(정수, 실수, 문자, 문자열 등)을 저장할 수 있는 공간의 별명이라고 할 수 있다. 어떤 값을 저장했다가 다시 사용하기 위해서 변수를 사용한다. 저장할 내용들이 많으면 필요한 만큼 변수를 만들어 사용하면 된다. 변수는 포스트 잇과 같은 메모지에 필요한 내용을 적어두었다가, 필요할 때 찾아 살펴보는 것과 비슷하다.

# 대수학(algebra)에서는 어떤 수나 값을 대신해 문자로 표현하는 방법을 사용한다.  프로그래밍언어에서도 마찬가지로 자신이 알아보기 쉬운 짧은 단어를 사용하는 것이 좋다. 예시) y = x + 3

### 정답
# c = input()
# print(c)

#
#
#
#

### 6010 : [기초-입출력] 정수 1개 입력받아 int로 변환하여 출력하기(설명)(py)

# 정수(integer)는 양의 정수(1, 2, 3, 4, 5, ...), 음의 정수(-1, -2, -3, -4, -5, ...), 0 과 같이 소숫점 아래에 수가 없는 수라고 할 수 있다.

# 변수에 정수값을 저장한 후 정수로 변환하여 출력해보자.

# 참고

# input() 을 사용하면 키보드로 입력(input)한 값을 가져온다.
# 변수 = input()
# 를 실행시키면 키보드로 입력한 값을 왼쪽의 변수에 저장(할당, asign) 한다.

# 변수는 어떤 값(정수, 실수, 문자, 문자열 등)을 저장할 수 있는 공간의 별명이라고 할 수 있다. 변수는 일반적으로 알파벳(a~z, A~Z)이나 언더라인 '_'으로 시작하는 단어를 사용하고, 숫자(0~9)로 시작하는 단어는 사용할 수 없다. 숫자로 시작하는 단어는 수로 인식하기 때문이다. (python의 경우 한글 변수도 사용할 수 있지만, 영문을 사용하는 것이 예상하지 못하는 오류를 방지할 수 있다.)

# '=' 연산자는 오른쪽의 계산 결과 값을 왼쪽의 변수에 저장하라는 의미의 대입연산자이다.
# 왼쪽의 결과값과 오른쪽의 결과값이 같다는 의미의 수학식의 등호와는 의미가 다르다.

### 정답
# n = input()
# n = int(n)
# print(n)

#
#
#
#

### 6011 : [기초-입출력] 실수 1개 입력받아 변환하여 출력하기(설명)(py)

# 숫자(0~9)와 소수점(.)을 사용해 표현한 수를 실수(real number)라고 한다.

# 변수에 실수값을 저장한 후 변수에 저장되어 있는 값을 그대로 출력해보자.

# 참고
# 어떤 값을 1개 입력받아 계산하거나 처리해야하는 경우라면, 입력되는 값이 수인지 문자열인지 구분해야한다. 조금 생각해보면, 키보드로 입력한 9라는 값이 문자 9인지, 정수 9인지, 실수 9.0인지 컴퓨터가 스스로 구분하지 못한다는 것을 알 수 있다. 컴퓨터 내부에서는 2진 체계의 디지털 형태로만 저장할 수 있기 때문에 정수, 문자, 실수 등의 저장 방법이 다르다. 입력한 값을 원하는 형태로 계산하거나 처리하기 위해서는 입력한 값이 어떤 데이터(정수, 문자, 실수, 문자열 등)인지 명확히 구분해 주어야 한다.

### 정답
# f = input()
# f = float(f)
# print(f)

#
#
#
#

### 6012 : [기초-입출력] 정수 2개 입력받아 그대로 출력하기1(설명)(py)

# 줄을 바꿔 정수(integer) 2개를 입력받아 줄을 바꿔 출력해보자.

### 정답
# a = input()
# b = input()
# a = int(a)
# b = int(b)
# print(a)
# print(b)

#
#
#
#

### 6013 : [기초-입출력] 문자 2개 입력받아 순서 바꿔 출력하기1(py)

# 줄을 바꿔 문자(character) 2개를 입력받고, 순서를 바꿔 한 줄씩 출력해보자.

### 정답
# a = input()
# b = input()
# print(b)
# print(a)

#
#
#
#

### 6014 : [기초-입출력] 실수 1개 입력받아 3번 출력하기(py)

# 실수(real number) 1개를 입력받아 줄을 바꿔 3번 출력해보자.

### 정답
# f = input()
# f = float(f)
# print(f)
# print(f)
# print(f)

#
#
#
#

### 6015 : [기초-입출력] 정수 2개 입력받아 그대로 출력하기2(설명)(py)

# 공백을 두고 입력된정수(integer) 2개를 입력받아 줄을 바꿔 출력해보자.

# 참고
# python의 input()은 한 줄 단위로 입력을 받는다.
# input().split() 를 사용하면, 공백을 기준으로 입력된 값들을 나누어(split) 자른다.
# a, b = 1, 2
# 를 실행하면, a에는 1 b에는 2가 저장된다.
# (주의 : 하지만, 다른 일반적인 프로그래밍언어에서는 이러한 방법을 지원하지 않기 때문에 a=1, b=2 를 한 번에 하나씩 따로 실행시켜야 한다.)

### 정답
# a, b = input().split()
# a = int(a)
# b = int(b)
# print(a)
# print(b)

#
#
#
#

### 6016 : [기초-입출력] 문자 2개 입력받아 순서 바꿔 출력하기2(설명)(py)

# 공백을 두고 문자(character) 2개를 입력받아 순서를 바꿔 출력해보자.

# 참고
# ...
# print(c2, c1)
# 와 같은 방법으로 출력하면, c1과 c2에 저장된 값이 공백을 두고 순서가 바뀌어 한 줄로 출력된다.
# print( ) 안에서 쉼표(,)를 찍어 순서대로 나열하면, 그 순서대로 공백을 두고 출력된다.

### 정답
# c1, c2 = input().split()
# print(c2, c1)

#
#
#
#

### 6017 : [기초-입출력] 문장 1개 입력받아 3번 출력하기(설명)(py)

# 정수(integer), 실수, 문자(character), 문자열(string) 등 1개만 입력받아 한 줄로 3번 출력해보자.

# 참고
# python 언어에서는 문자/정수/실수/문자열 등 특별한 구분이 없이도 원하는 변수에 저장시켜 출력 할 수 있다.
# 하지만, 저장된 값을 이용해 계산하거나 서로 붙여 연결시키거나 잘라내는 작업을 한다면?
# 반드시 저장되어있는 값의 종류(문자/정수/실수/문자열 등)를 구분해 주어야 한다.

### 정답
# s = input()
# print(s, s, s)

#
#
#
#

### 6018 : [기초-입출력] 시간 입력받아 그대로 출력하기(설명)(py)

# 24시간 시:분 형식으로 시간이 입력될 때, 그대로 출력하는 연습을 해보자.

# 참고
# input().split(':') 를 사용하면 콜론 ':' 기호를 기준으로 자른다.
# print(?, ?, sep=':') 를 사용하면 콜론 ':' 기호를 사이에 두고 값을 출력한다.
# sep 는 분류기호(seperator)를 의미한다.

### 정답
# hour, min = input().split(':')
# print(hour, min, sep=':')

#
#
#
#

### 6019 : [기초-입출력] 연월일 입력받아 순서 바꿔 출력하기(py)

# "연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자.

# 참고
# y, m, d = input().split('.')
# 과 같이 변수들을 순서대로 나열하면 구분기호를 기준으로 잘라 순서대로 저장한다.

### 정답
# y, m, d = input().split('.')
# print(d, m, y, sep='-')

#
#
#
#

### 6020 : [기초-입출력] 주민번호 입력받아 형태 바꿔 출력하기(py)

# 주민번호는 다음과 같이 구성된다.
# XXXXXX-XXXXXXX
# 왼쪽 6자리는 생년월일(YYMMDD)이고, 오른쪽 7자리는 성별,출생지역,확인코드로 구성되어있다.

# 주민번호를 입력받아 '-'를 제외한 주민번호 13자리를 모두 붙인 형태로 바꿔 출력해보자.

# 참고
# 아무것도 없는 공(empty) 문자는 작은 따옴표(') 2개를 붙여서 '' 로 표현한다.

### 정답
# first, last = input().split('-')
# print(first, last, sep='')

#
#
#
#

### 6021 : [기초-입출력] 단어 1개 입력받아 나누어 출력하기(설명)(py)

# 알파벳과 숫자로 이루어지며 5개의 문자로 이루어진 단어 1개가 입력된다.
# 입력받은 단어의 각 문자를 한 줄에 한 문자씩 분리해 출력한다.

# 참고
# s[0] 은 입력받은 문자열 s 의 첫 번째 문자를 의미한다.

### 정답
# s = input()
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4])

#
#
#
#

### 6022 : [기초-입출력] 연월일 입력받아 나누어 출력하기(설명)(py)

# 6자리의 연월일(YYMMDD)을 입력받아 년도(YY) 월(MM) 일(DD)을 공백으로 구분해 한 줄로 출력해보자.

# 참고
# s = input()
# print(s[0:2])
# 를 실행하면 0번째 문자부터 1번째 문자까지 잘라 출력한다.
# s[a:b] 라고 하면, s라는 단어에서 a번째 문자부터 b-1번째 문자까지 잘라낸 부분을 의미한다.
# 다른 자르기 방법도 있다.

### 정답
# s = input()
# print(s[0:2], s[2:4], s[4:6], sep=' ')

#
#
#
#

### 6023 : [기초-입출력] 시분초 입력받아 분만 출력하기(py)

# 시:분:초 형식으로 시간이 입력될 때 분만 출력해보자.

# 어떻게 분만 출력해야 할지 주의 깊게 생각해야한다.

### 정답
# h, m, s = input().split(':')
# print(m)

#
#
#
#

### 6024 : [기초-입출력] 단어 2개 입력받아 이어 붙이기(설명)(py)

# 알파벳 문자와 숫자로 이루어진 단어 2개를 입력받아
# 순서대로 붙여 출력하는 프로그램을 작성해보자.

# 참고
# 단어는 문자(character)들로 만든다.
# 문자들로 구성된 문장을 문자열(string)이라고 부른다.
# 문자열에는 공백문자(' ')가 포함될 수 있는데, 문자 1개는 길이가 1인 문자열이라고 할 수 있고, 공백문자(' ')가 없는 문자열은 단어(word)라고 할 수 있다.

# 일반적인 문장들은 공백으로 구분된 단어들로 만들어지기 때문에, 공백문자로 구분된 문장에서 단어를 잘라내기 위해서는 공백문자(' ')를 기준으로 자르면 된다. 키보드로 입력되는 것들은 기본적으로 문자열로 인식되고, 문자열끼리 더하기(+)를 실행하면, 두 문자열을 합쳐 연결한(concatenate) 결과를 만들어 낸다.

### 정답
# s = input().split(' ')
# print(s[0] + s[1])

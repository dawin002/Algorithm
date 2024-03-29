""" 6077 : [기초-종합] 짝수 합 구하기 """

# 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.

# 방법1 : for 문
# n = int(input())
# sum = 0
# for i in range(n+1) :
#   if i%2 == 0 :
#     sum += i
# print(sum)

# 방법2 : while 문
# n = int(input())
# sum = 0
# i = 2
# while i <= n :
#   sum += i
#   i += 2
# print(sum)

#
#
#
#
""" 6078 : [기초-종합] 원하는 문자가 입력될 때까지 반복 출력하기 """

# 영문 소문자 'q'가 입력될 때까지
# 입력한 문자를 계속 출력하는 프로그램을 작성해보자.

# c = 'a'
# while c != 'q' :
#   c = input()
#   print(c)

#
#
#
#
""" 6079 : [기초-종합] 언제까지 더해야 할까? """

# 1, 2, 3 ... 을 계속 더해 나갈 때,
# 그 합이 입력한 정수(0 ~ 1000)보다 작을 때까지만
# 계속 더하는 프로그램을 작성해보자.

# 즉, 1부터 n까지 정수를 계속 더해 나간다고 할 때,
# 어디까지 더해야 입력한 수보다 같거나 커지는 지를 알아보고자하는 문제이다.

# n = int(input())
# i = 0
# sum = 0
# while sum < n :
#   i += 1
#   sum += i
# print(i)

# n = int(input())
# sum = 0
# for i in range(100) :
#   i += 1
#   sum += i
#   if sum >= n :
#     break
# print(i)

#
#
#
#
""" 6080 : [기초-종합] 주사위 2개 던지기 """

# 1부터 n까지, 1부터 m까지 숫자가 적힌 서로 다른 주사위 2개를 던졌을 때,
# 나올 수 있는 모든 경우를 출력해보자.

# rg1, rg2 = input().split(' ')
# rg1 = int(rg1)
# rg2 = int(rg2)
# for r1 in range(1, rg1 + 1):
#   for r2 in range(1, rg2 + 1):
#     print(r1, r2, sep=' ')

#
#
#
#
""" 6081 : [기초-종합] 16진수 구구단 출력하기 """

# 16진수(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F)를 배운
# 영일이는 16진수끼리 곱하는 16진수 구구단?에 대해서 궁금해졌다.

# A, B, C, D, E, F 중 하나가 입력될 때,
# 1부터 F까지 곱한 16진수 구구단의 내용을 출력해보자.
# (단, A ~ F 까지만 입력된다.)

# 참고
# print('%X'%n)    #n에 저장되어있는 값을 16진수(hexadecimal) 형태로 출력
# 작은 따옴표 2개를 사용해서 print(..., sep='') 으로 출력하면, 공백없이 모두 붙여 출력된다.
# 작은 따옴표 2개 '' 또는 큰 따옴표 2개 "" 는 아무 문자도 없는 빈문자열(empty string)을 의미한다.

# a = int(input(), 16)
# for i in range(1, 16) :
#   print('%X'%a, '*', '%X'%i, '=', '%X'%(a*i), sep='')
""" 
  print("%X*%X=%X"%(n,i,n*i)) 로 쓰는게 더 정확함 
  "" 안의 %X 는 문자열과 분리 안해줘도 되어서
  " %X * %X = %X " %(a, i, n*i) 로 서식 지정 가능
"""

#
#
#
#

""" 6082 : [기초-종합] 3 6 9 게임의 왕이 되자(설명) """

# 친구들과 함께 3 6 9 게임을 하던 영일이는 잦은 실수 때문에 계속해서 벌칙을 받게 되었다.
# 3 6 9 게임의 왕이 되기 위한 369 마스터 프로그램을 작성해 보자.

# 만약 3, 6, 9 가 들어간 수를 자신이 불러야 하는 상황이라면, 수를 부르는 대신 "박수(X)" 를 쳐야 한다.
# 33과 같이 3,6,9가 두 번 들어간 수 일때, "짝짝"과 같이 박수를 두 번 치는 형태도 있다.

""" 내 풀이 : 정수 나눗셈 몫, 나머지 이용 방식 """
# n = int(input())
# for i in range(1, n+1) :
#   checkX = 0
#   ori = i
#   while i > 0 :
#     if i%10%3 == 0 and i%10!=0 :
#       checkX = 1
#       print('X', end='')
#     i = i // 10
#   if checkX == 0 :
#     print(ori, end='')
#   print(' ', end='')

""" 내 풀이 : 문자열 분리 방식 """
# n = int(input())
# for i in range(1, n+1) :
#   i = str(i)
#   out = ""
#   for c in range(len(i)) :
#     c = int(i[c])
#     if c%3==0 and c!=0 :
#       out += "X"
#   if out != "" :
#     print(out, end=' ')
#   else :
#     print(i, end=' ')

#
#
#
#

""" 6083 : [기초-종합] 빛 섞어 색 만들기 """
# 빨강(red), 초록(green), 파랑(blue) 빛을 섞어 여러 가지 다른 색 빛을 만들어 내려고 한다.

# 빨강(r), 초록(g), 파랑(b) 각 빛의 가짓수가 주어질 때,
# 주어진 rgb 빛들을 섞어 만들 수 있는 모든 경우의 조합(r g b)과 만들 수 있는 색의 가짓 수를 계산해보자.

# r, g, b = input().split(' ')
# r = int(r)
# g = int(g)
# b = int(b)
# for i in range(r) :
#   for j in range(g) :
#     for k in range(b) :
#       print("%d %d %d" %(i, j, k))
# print(r*g*b)

#
#
#
#

""" 6084 : [기초-종합] 소리 파일 저장용량 계산하기 """

# 소리가 컴퓨터에 저장될 때에는 디지털 데이터화 되어 저장된다.

# 마이크를 통해 1초에 적게는 수십 번, 많게는 수만 번 소리의 강약을 체크하고,
# 한 번씩 체크할 때 마다 그 값을 정수값으로 바꾸어 저장하는 방식으로 소리를 파일로 저장할 수 있다.

# 값을 저장할 때에는 비트를 사용하는 정도에 따라 세세한 녹음 정도를 결정할 수 있고,
# 좌우(스테레오) 채널로 저장하면 2배… 5.1채널이면 6배의 저장공간이 필요하고,
# 녹음 시간이 길면 그 만큼 더 많은 저장공간이 필요하다.

# 1초 동안 마이크로 소리강약을 체크하는 횟수를 h
# (헤르쯔, Hz 는 1초에 몇 번? 체크하는가를 의미한다.)

# 한 번 체크한 값을 저장할 때 사용하는 비트수를 b
# (2비트를 사용하면 0 또는 1 두 가지, 16비트를 사용하면 65536가지..)

# 좌우 등 소리를 저장할 트랙 개수인 채널 개수를 c
# (모노는 1개, 스테레오는 2개의 트랙으로 저장함을 의미한다.)

# 녹음할 시간(초) s가 주어질 때,

# 필요한 저장 용량을 계산하는 프로그램을 작성해보자.

# 실제로, 일반적인 CD 음질(44.1KHz, 16bit, 스테레오)로 1초 동안 저장하려면
# 44100 * 16 * 2 * 1 bit의 저장공간이 필요한데,
# 44100*16*2*1/8/1024/1024 로 계산하면 약 0.168 MB 정도가 필요하다.

# 이렇게 녹음하는 방식을 PCM(Pulse Code Modulation) 방법이라고 하는데,
# 압축하지 않은 순수한(raw) 소리 데이터 파일은 대표적으로 *.wav 가 있다.

# **
#       8 bit(비트)           = 1byte(바이트)       # 8bit=1Byte
# 1024 Byte(210 byte) = 1KB(킬로 바이트)  # 1024Byte=1KB
# 1024 KB(210 KB)      = 1MB(메가 바이트)
# 1024 MB(210 MB)     = 1GB(기가 바이트)
# 1024 GB(210 GB)      = 1TB(테라 바이트)

# h, b, c, s = input().split(' ')
# h = int(h)
# b = int(b)
# c = int(c)
# s = int(s)
# mb = h * b * c * s / 8 / 1024 / 1024
# print(round(mb, 1), "MB")

#
#
#
#

""" 6085 : [기초-종합] 그림 파일 저장용량 계산하기 """

# 이미지가 컴퓨터에 저장될 때에도 디지털 데이터화 되어 저장된다.
# 가장 기본적인 방법으로는 그림을 구성하는 한 점(pixel, 픽셀)의 색상을
# 빨강(r), 초록(g), 파랑(b)의 3가지의 빛의 세기 값으로 따로 변환하여 저장하는 것인데,
# 예를 들어 r, g, b 각 색에 대해서 8비트(0~255, 256가지 가능)씩을 사용한다고 하면,
# 한 점의 색상은 3가지 r, g, b의 8비트+8비트+8비트로 총 24비트로 표현해서
# 총 2^24 가지의 서로 다른 빛의 색깔을 사용할 수 있는 것이다.
# 그렇게 저장하는 점을 모아 하나의 큰 이미지를 저장할 수 있게 되는데,
# 1024 * 768 사이즈에 각 점에 대해 24비트로 저장하면 그 이미지를 저장하기 위한
# 저장 용량을 계산할 수 있다.
# 이렇게 이미지의 원래(raw) 데이터를 압축하지 않고 그대로 저장하는 대표적인 이미지 파일이
# *.bmp 파일이며, 비트로 그림을 구성한다고 하여 비트맵 방식 또는 래스터 방식이라고 한다.

# 이미지의 가로 해상도 w, 세로 해상도 h, 한 픽셀을 저장하기 위한 비트 b 가 주어질 때,
# 압축하지 않고 저장하기 위해 필요한 저장 용량을 계산하는 프로그램을 작성해 보자.

# 예를 들어
# 일반적인 1024 * 768 사이즈(해상도)의 각점에 대해
# 24비트(rgb 각각 8비트씩 3개)로 저장하려면
# 1024 * 768 * 24 bit의 저장공간이 필요한데,
# 1024*768*24/8/1024/1024 로 계산하면 약 2.25 MB 정도가 필요하다.

# 실제 그런지 확인하고 싶다면, 간단한 그림 편집/수정 프로그램을 통해 확인할 수 있다.

# **
#       8 bit(비트)           = 1byte(바이트)     #       8bit=1Byte
# 1024 Byte(210 byte) = 1KB(킬로 바이트)  # 1024Byte=1KB
# 1024 KB(210 KB)      = 1MB(메가 바이트)
# 1024 MB(210 MB)     = 1GB(기가 바이트)
# 1024 GB(210 GB)      = 1TB(테라 바이트)

# w, h, b = input().split(' ')
# w = int(w)
# h = int(h)
# b = int(b)
# mb = w * h * b / 8 / 1024 / 1024
# print(f"{mb:.2f} MB")

""" f-string 을 사용해 서식 지정 """
"""
    hi = 170.0000001
    we = 65.0000001
    --> 키는 170.00 이고 몸무게는 65.00 이야~
    print( f" 키는 {hi:.2f} 이고 몸무게는 {we:.2f} 이야~ ")
    print( " 키는 {:.2f} 이고 몸무게는 {:.2f} 이야~ ".format(hi, we))
    print( " 키는 {0:.2f} 이고 몸무게는 {1:.2f} 이야~ ".format(hi, we))
    print( " 키는 {1:.2f} 이고 몸무게는 {0:.2f} 이야~ ".format(we, hi))
    print( " 키는 ", format(hi, ".2f"), " 이고 몸무게는 ", format(we, ".2f"), " 이야~ ")
"""

#
#
#
#

""" 6086 : [기초-종합] 거기까지! 이제 그만~ """

# 1, 2, 3 ... 을 순서대로 계속 더해 합을 만드는데,
# 그 합이 입력한 정수보다 작을 동안만 계속 더하는 프로그램을 작성해보자.

# 즉, 1부터 n까지 정수를 하나씩 더해 합을 만드는데,
# 어디까지 더해야 입력한 수보다 같거나 커지는지 알아보고자 하는 문제이다.

# 하지만, 이번에는 그 때 까지의 합을 출력해야 한다.

# 예를 들어, 57을 입력하면
# 1+2+3+...+8+9+10=55에서 그 다음 수인 11을 더해 66이 될 때,
# 그 값 66이 출력되어야 한다.

# n = int(input())
# sum = i = 0
# while sum < n :
#   i += 1
#   sum += i
# print(sum)

#
#
#
#

""" 6087 : [기초-종합] 3의 배수는 통과 """

# 1부터 입력한 정수까지 1씩 증가시켜 출력하는 프로그램을 작성하되,
# 3의 배수인 경우는 출력하지 않도록 만들어보자.

# 예를 들면,
# 1 2 4 5 7 8 10 11 13 14 ...
# 와 같이 출력하는 것이다.

""" 방법1 : 반복하며 계속 바로 출력 (얘가 더 빨랐음 이유는 ?) """
# n = int(input())
# for i in range(1, n+1) :
#   if i%3 != 0 :
#     print(i, end=' ')

""" 방법2 : 반복하며 더해서 한번만 출력 """
# n = int(input())
# str1 = ""
# for i in range(1, n+1) :
#   if i%3 != 0 :
#     str1 += str(i) + " "
# print(str1)

""" 
    특이한 방법 !!! 
    리스트에 추가 후 리스트 요소들 공백으로 띄워서 출력
    리스트 안에 있는 숫자들을 공백으로 띄워서 출력하고 싶을 때, unpacking을 사용해서 해결할 수 있습니다.
"""
# n = int(input())
# res = []
# for i in range(1, n+1):
#     if i%3 != 0: res.append(i)
# print(*res)

#
#
#
#

""" 6088 : [기초-종합] 수 나열하기1 """

# 어떤 규칙에 따라 수를 순서대로 나열한 것을 수열(sequences)이라고 한다.

# 예를 들어
# 1 4 7 10 13 16 19 22 25 ... 은
# 1부터 시작해 이전에 만든 수에 3을 더해 다음 수를 만든 수열이다.
# 이러한 것을 수학에서는 앞뒤 수들의 차이가 같다고 하여

# 등차(차이가 같다의 한문 말) 수열이라고 한다. (등차수열 : arithmetic progression/sequence)
# 수열을 알게 된 영일이는 갑자기 궁금해졌다.

# "그럼.... 123번째 나오는 수는 뭘까?"

# 영일이는 프로그램을 만들어 더 큰 수도 자동으로 계산하고 싶어졌다.

# 시작 값(a), 등차(d), 몇 번째인지를 나타내는 정수(n)가 입력될 때
# n번째 수를 출력하는 프로그램을 만들어보자.

# a, d, n = input().split()
# a = int(a)
# d = int(d)
# n = int(n)
# print(a + d * (n-1))
""" 
    a, d, n = input().split(' ') 으로 하면 split(' ') 에서 에러남
    이유는 입력에서 "1 3 2 " 로 공백이 하나 들어와 항목이 4개로 계산된 것
    split() 사용하니 에러 안남
"""

#
#
#
#

""" 6089 : [기초-종합] 수 나열하기2 """

# 2 6 18 54 162 486 ... 은
# 2부터 시작해 이전에 만든 수에 3을 곱해 다음 수를 만든 수열이다.

# 이러한 것을 수학에서는 앞뒤 수들의 비율이 같다고 하여
# 등비(비율이 같다의 한문 말) 수열이라고 한다. (등비수열 : geometric progression/sequence)

# 등비 수열을 알게된 영일이는 갑자기 궁금해졌다.
# "그럼.... 13번째 나오는 수는 뭘까?"
# 영일이는 프로그램을 만들어 더 큰 수도 자동으로 계산하고 싶어졌다.

# 시작 값(a), 등비(r), 몇 번째인지를 나타내는 정수(n)가 입력될 때
# n번째 수를 출력하는 프로그램을 만들어보자.

# a, r, n = input().split()
# a = int(a)
# r = int(r)
# n = int(n)
# print( a * r ** (n-1))

#
#
#
#

""" 6090 : [기초-종합] 수 나열하기3 """

# 1 -1 3 -5 11 -21 43 ... 은
# 1부터 시작해 이전에 만든 수에 -2를 곱한 다음 1을 더해 다음 수를 만든 수열이다.

# 이런 이상한 수열을 알게 된 영일이는 또 궁금해졌다.
# "그럼.... 13번째 나오는 수는 뭘까?"

# 영일이는 물론 수학을 아주 잘하지만 이런 문제는 본 적이 거의 없었다...
# 그래서 프로그램을 만들어 더 큰 수도 자동으로 계산하고 싶어졌다.

# 시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째인지를 나타내는 정수(n)가 입력될 때,
# n번째 수를 출력하는 프로그램을 만들어보자.

# a, m, d, n = map(int, input().split())
# res = a
# for i in range(1, n) :
#   res = res * m + d
# print(res)

""" 
    정수 여러 개 입력받을 때 
    a, b, c = map(int, input().split()) 를 써보자
"""

#
#
#
#

""" 6091 : [기초-종합] 함께 문제 푸는 날 """

# 온라인 채점시스템에는 초등학생, 중고등학생, 대학생, 대학원생,
# 일반인, 군인, 프로그래머, 탑코더 등 아주 많은 사람들이 들어와 문제를 풀고 있는데,

# 실시간 채점 정보는 메뉴의 채점기록(Judge Status)을 통해 살펴볼 수 있다.

# 자! 여기서...잠깐..
# 같은 날 동시에 가입한 3명의 사람들이 온라인 채점시스템에 들어와 문제를 푸는 날짜가
# 매우 규칙적이라고 할 때, 다시 모두 함께 문제를 풀게 되는 그날은 언제일까?

# 예를 들어 3명이 같은 날 가입/등업하고, 각각 3일마다, 7일마다, 9일마다
# 한 번씩 들어온다면, 처음 가입하고 63일 만에 다시 3명이 함께 문제를 풀게 된다.

# 갑자기 힌트?
# 왠지 어려워 보이지 않는가?
# 수학에서 배운 최소공배수를 생각한 사람들도 있을 것이다. 하지만, 정보에서 배우고 경험하는
# 정보과학의 세상은 때때로 컴퓨터의 힘을 빌려 간단한 방법으로 해결할 수 있게 한다.

# 아래의 코드를 읽고 이해한 후 도전해 보자.
# day는 날 수, a/b/c는 방문 주기이다.

# a, b, c = map(int, input().split())
# day = 1
# while True :
#   if day%a==0 and day%b==0 and day%c==0 :
#     break
#   day += 1
# print(day)

""" 아래 while문 써도 가능함 """
# while d%a!=0 or d%b!=0 or d%c!=0 :
#   d += 1

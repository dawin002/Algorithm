""" 2444: 별 찍기 - 7 """

import sys
input = sys.stdin.readline

n = int(input())
for i in range(1, n+1):
    print(' ' * (n - i), '*' * (i * 2 - 1), sep='')
for i in range(n-1, 0, -1):
    print(' ' * (n - i), '*' * (i * 2 - 1), sep='')

"""
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""
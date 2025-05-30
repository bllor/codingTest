'''

3
2 2
11 11

2 3 4

4
3 3
22 22
11 11 11 11
'''
import sys
n,k = map(int, sys.stdin.readline().split(' '))
sn = 2**(n-1)
print(k//sn)

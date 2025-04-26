import sys
N = int(input())
watt,volt = map(int,sys.stdin.readline().split(' '))
adapter = 0

if N<=(watt/volt):
    adapter=1
print(adapter)
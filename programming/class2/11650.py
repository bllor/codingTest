import sys
# arr = [[1,-1],[3,2],[1,1],[3,4],[2,2]]
# arr.sort()
# print(arr)
N = int(input())
arr = [None]*N
for i in range(N):
    x,y = map(int, sys.stdin.readline().split(' '))
    arr[i] = [x,y]
arr.sort()
# print(arr)
for xy in arr:
    print(xy[0],xy[1])
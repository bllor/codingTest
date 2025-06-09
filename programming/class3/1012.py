# arr=[[1,2,3],[4,5,6],[7,8,9]]
# print(arr[0][1])

import sys
input  = sys.stdin.readline
T  = 1
M,N,K = map(int,input().split(' '))
arr = [[0] * M for _ in range(N+1)]

for i in range(K):
    x,y = map(int,input().split(' '))
    arr[x][y] = 1

print(arr)
for i in range(M):
    for j in range(N-1):
        print(i,j,arr[i][j])
            


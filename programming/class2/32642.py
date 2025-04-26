import sys
N = int(input())
arr = list(map(int,sys.stdin.readline().split(' ')))
arr2 = [0]*N
a = 0

for i in range(N):
    if arr[i] == 0:
        a-=1
        arr2[i] = a
    else:
        a += 1
        arr2[i] = a
print(sum(list(arr2)))        
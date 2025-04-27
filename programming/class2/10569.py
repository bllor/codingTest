N = int(input())
arr=[None]*N
for i in range(N):
    v,e = map(int,input().split(' '))
    arr[i] = [v,e]
for i in range(N):
    print(2+arr[i][1]-arr[i][0])
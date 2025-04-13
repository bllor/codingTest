a,b,c,d = map(int,input().split(' '))
t1 =0
t2 =0

arr=[a,b,c,d]
arr.sort()
print(abs(arr[0]+arr[3]-arr[1]-arr[2]))
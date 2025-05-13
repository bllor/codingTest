N = int(input())
arr=[None]*N

for i in range(N):
     arr[i]=input()
    
for t in arr:
    h,w,n = map(int,t.split(' '))
    # print(n/h)
    # print(n//h)
    # print(n%h)
    f = 0
    if n%h ==0 :
        f = h
    else:
        f = n%h
    
    r = 0 
    if n/h>n//h:
        r = n//h+1
    else:
        r = n//h
    if r<10:
        r = '0'+str(r)
    else:
        r= str(r)
    print(str(f)+r)
    
k,n = map(int, input().split(' '))
arr = [None]*k

for i in range(k):
    arr[i] = int(input())

maxNo = sum(arr)//n
tn = 0
for mno in range(maxNo,1,-1):
    ntm = 0
    for i in range(k):
        ntm+=arr[i]//mno  
    if ntm>=n and mno>tn:
        tn=mno
        break
print(tn)        
        
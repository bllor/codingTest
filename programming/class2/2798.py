n,m = map(int,input().split(' '))

arr = [None]*n

arr = list(map(int,input().split(' ')))

maxNumber = 0

tn = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            tn+=1
            if i==j or i==k or j==k :
                continue
            if arr[i]+arr[j]+arr[k] > m:
                continue
            elif arr[i]+arr[j]+arr[k] > maxNumber:
                maxNumber = arr[i]+arr[j]+arr[k]
print('총연산횟수',tn)
print(maxNumber)
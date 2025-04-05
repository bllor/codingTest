n = int(input())
arr = [None]*n

arr = list(map(int,input().split(' ')))
pn = 0
for i in arr:
    if i==1:
        continue
    elif i==2:
        pn+=1
    else:
        for j in range(2,i):
            if i-1 ==j:
                pn+=1
            elif i%j ==0:
                break
            else:
                continue
print(pn)
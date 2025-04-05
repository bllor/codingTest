n = int(input())
arr = [None]*n

arr = list(map(int,input().split(' ')))
pn = 0
for i in arr:
    if i==1:
        continue
    elif i==2 or i==3:
        pn+=1
    else:
        midNumber = i//2+1
        for j in range(2,midNumber):
            if i%j ==0:
                break
            elif midNumber-1 ==j:
                pn+=1
            else:
                continue
print(pn)
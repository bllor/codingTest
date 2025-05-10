N = int(input())

# N = 18

n = 0
if N//5>0:
    n=  N//5
else:
    n = 0
n2 = N//3

tn= -1
for i in range(n,-1,-1):
    for j in range(n2,-1,-1):
        if 5*int(i)+3*int(j)==N:
            if tn==-1:
                tn=i+j
            if tn>i+j:
                tn=i+j

print(tn)
    
    

    
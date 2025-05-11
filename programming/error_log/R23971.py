H,W,N,M = map(int,input().split(' '))

rn = 0
cn = 0
for i in range(0,H,N+1):
    # print(i)
    rn+=1
for j in range(0,W,M+1):
    # print(j)
    cn+=1

print(rn*cn)
    

n1 = int(input())
n2 = int(input())
n3 = int(input())

n4 = (n1*n2*n3)

d1= [0 for i in range(10)]

for i in range(len(str(n4))):
    for j in range(len(d1)):
        # print("j",j,"str(n4)[i]",str(n4)[i])
        if str(n4)[i]==str(j):
            d1[j]+=1
            break
        
for i in range(len(d1)):
    print(d1[i])
a = True

b=[]
i=0
while a:
    if i ==28:
        break
        a=False
    n = int(input())
    b.append(n)
    i+=1

c = [i for i in range(1,31)]
d = c
for j in range(len(b)):
    if b[j] in c:
        d.remove(b[j])


for i in range(len(d)):
    print(d[i])
         
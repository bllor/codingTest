d = [1,1,2,2,2,8]
c =  input().split(' ')

for i in range(len(c)):
    d[i]=int(d[i])-int(c[i])

print(list(d).join(" "))

for i in range(len(d)):
    print(d[i], end =' ')
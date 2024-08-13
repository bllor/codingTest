str= input()

d1 = [-1 for i in range(26)]

for i in range(len(d1)):
    for j in range(len(str)):
        if d1[i]== -1 and i==(int(ord(str[j])-97)):
            d1[i]=j

for i in range(len(d1)):
    print(d1[i],end=' ')
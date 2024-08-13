n = int(input())

for i in range(n):
    str = input()
    d=0
    s=0
    for j in range(len(str)):
        if str[j]=='O':
            d+=1+s
            s+=1
        else:
            s=0
    print(d)
    
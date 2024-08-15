n = int(input())
tn =0

for a in range(n):
    str = input()
    d = {}
    tf = True
    for i in range(len(str)):
        if  str[i] not in d.keys():
            d[str[i]]=i
        else:
            if d[str[i]] ==i-1:
                d[str[i]]=i
            else:
                tf = False
                break
    if tf :
        tn+=1
print(tn)

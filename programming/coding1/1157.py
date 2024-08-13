str = input()

str = str.upper()

di = {}
for i in range(len(str)):
    if str[i] not in di.keys():
        di[str[i]]=1
    else:
        di[str[i]]+=1

max = 0
maxkey =''
for key,value in di.items():
    if max<value:
        max = value
        maxkey=key
    elif max==value:
        maxkey+=key

print(maxkey if len(maxkey)==1 else '?')
n = int(input())

tn = 1
ts = 1 

while tn <= n:
    if tn>=n:
        break
    else:
        tn+=(ts)*6
        ts+=1

print(ts)

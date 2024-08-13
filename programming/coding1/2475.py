nzip = input().split(' ')

d = 0
for i in range(len(nzip)):
    d+=int(nzip[i])**2
print(d%10)
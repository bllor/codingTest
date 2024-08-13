n, m = map(int, input().split(' '))

li = [i+1 for i in range(n)]
for q in range(m):
    i, j = map(int, input().split(" "))
    if abs(j-i)<2:
        t= li[j-1]
        li[j-1] =li[i-1]
        li[i-1] = t
    else:
        for w in range((j-i+1)//2):
            t= li[i+w-1]
            li[i+w-1] =li[j-w-1]
            li[j-w-1]=t

for l in li:
    print(l,end = ' ') 
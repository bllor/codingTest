n,m = map(int, input().split(' '))

str = [i+1 for i in range(n)]

for a in range(m):
    i , j = map(int, input().split(' '))
    t = str[i-1]
    str[i-1]= str[j-1]
    str[j-1]=t                
    
print(str)

for q in str:
    print(q,end =" ")
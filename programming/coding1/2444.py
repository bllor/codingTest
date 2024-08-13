n = int(input())

for i in range(n):
    print(' '*(n-i-1)+'*'*(i+1)+'*'*(i))
for j in range(n-1):
    print(' '*(j+1)+'*'*(n-1-j)+'*'*(n-2-j))
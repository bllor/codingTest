n = int(input())

for i in range(n):
    n1 = 2*(1+i)-1
    n2 = n-1-i
    print(' '*n2+'*'*n1)
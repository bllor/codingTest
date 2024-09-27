n = int(input())

if n == 0:
    print(1)
else:
    max = 1
    for i in range(1,n+1,1):
        max=max*i
    print(max)
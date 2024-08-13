a=True
while a:
    n,m = map(int, input().split(' '))
    if n==0 and m==0:
        break
        a = False
    str = "Yes" if n>m else "No"
    print(str)
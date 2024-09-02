str = input()

a,b,c,d,e = str.split(' ')
if int(a)+int(c)==int(e):
    print('YES')
else:
    print('NO')
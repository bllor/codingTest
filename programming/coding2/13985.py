str = input()

a,b,c,d,e = str.split(' ')
print(a,b,c,d,e)
if int(a)+int(c)==int(e):
    print('YES')
else:
    print('NO')
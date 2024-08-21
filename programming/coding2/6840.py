a = int(input())
b = int(input())
c = int(input())

min = a
max = c

if min>b:
    min=b
if min>c:
    min = c

if max<a:
    max=a
if max<b:
    max= b

if a != min and a!= max:
    print(a)
elif b != min and b!= max:
    print(b)
else:
    print(c)
    
    
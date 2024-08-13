a  = map(int, input().split(' '))

b= 0

for i in a:
    if i ==9:
        b+=1
    else:
        continue

str = 'F' if b>0 else 'S'
print(str)
n,a,b = map(int, input().split(' '))

if a < (n+(b-n)):
    print("Bus")
elif a==(n+(b-n)):
    print("Anything")
else:
    print('Subway')


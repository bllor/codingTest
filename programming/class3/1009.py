N = int(input())

for no in range(N):
    a,b = map(int, input().split(' '))
    if b%4==0:
        c = 4
    else:
        c= b%4
    tn = a**c
    if tn%10 == 0 :
        print(10)
    else:
        print(tn%10)

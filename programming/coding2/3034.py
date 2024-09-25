n,w,h = map(int, input().split( ))

t =  (w**2+h**2)**(1/2)
for i in range(n) :
    inputValue = int(input())
    if t -inputValue >=0:
        print("DA")
    else:
        print("NE")    
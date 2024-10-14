def med3(a,b,c):
    mid = a
    if a<=b:
        if a>=c:
            mid = a
            return mid
        else:
            mid = c
            return mid
    if a<=c:
        if a>=b:
            mid = a
            return mid
        else:
            mid = b
            return mid
    
    if b<=c:
        if b>=a:
            mid = b
            return mid
        else:
            mid = a
            return mid


print(med3(1,3,2))
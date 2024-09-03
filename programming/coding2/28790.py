a,b,c = map(int, input().split(" "))

p = False
m = False
if a >=1000:
    p=True

if b>=8000 or c>=260:
    m = True

if p and m :
    print("Very Good")
elif p :
    print("Good")
else:
    print("Bad")

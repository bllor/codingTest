max = 0
p = 0
for i in range(9):
    n = int(input())
    if max < n:
        max = n
        p = i+1

print(max,'\n'+str(p))
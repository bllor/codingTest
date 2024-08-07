
a = []
for i in range(3):
    n = int(input())
    a.append(n%42)
    
a = set(a)
print(len(a))
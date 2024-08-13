n,m = input().split(' ')

nt,mt = n[2],m[2]
nt2,mt2=n[1],m[1]
nt3,mt3=n[0],m[0]
nn= nt+nt2+nt3
nm= mt+mt2+mt3
print(nn if nn>nm else nm)
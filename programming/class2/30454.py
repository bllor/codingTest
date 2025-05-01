# N,L = 5,9
# arr=[
# '110010101',
# '101010100',
# '000011111',
# '011011010',
# '100100101',    
# ]
N,L = map(int,input().split(' '))
arr = [None]*N
for i in range(N):
    arr[i] = input()
Z_arr = []

for i in range(N):
    noZ = False
    lno = 0
    for j in range(L):
        if arr[i][j] == '1' and not noZ:
        #    print('add')
           lno+=1
           noZ=True
        elif arr[i][j]=='1':
            continue
        else:
            # print('no',i,j,noZ)
            noZ = False
    Z_arr.append(lno)
    # print('----------------')
# print(Z_arr)

maxNo  = max(Z_arr)
# print(maxNo)
zno = 0

for no in Z_arr:
    if maxNo == no:
        zno+=1
print(maxNo,zno) 
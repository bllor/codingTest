import sys
N = int(input())
# N = 5
arr = [None]*N
# arr = [
# [55, 185],
# [58, 183],
# [88, 186],
# [60, 175],
# [46, 155]    
# ]
Karr = [None]*N
 
for i in range(N):
    x,y = map(int, sys.stdin.readline().split(' '))
    arr[i]=[x,y]
# print(arr)
for i in range(N):
    k = 1
    for j in range(N):
        # print(f'i:{i}, j:{j}')
        if arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1]:
            # print(arr[i][0],arr[j][0])
            k+=1
    Karr[i]=k
# print(Karr)
# print(''.join(str(Karr)))
for i in range(N):
    print(Karr[i], end=' ')
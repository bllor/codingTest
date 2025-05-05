import sys
# arr = list(map(int, sys.stdin.readline().split(' ') ))
arr = [None]*3
for i in range(3):
    arr[i] = list(map(int, sys.stdin.readline().split(' ') ))
# print(arr)
for row in arr:
    no1 = 0
    for stick in row:
        if stick == 1:
            no1+=1        
    if no1 == 4:
        print('E')
    elif no1 == 3:
        print('A')
    elif no1 == 2:
        print('B')
    elif no1 ==1 :
        print('C')
    else:
        print('D')

        
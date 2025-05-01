arr = list(map(int, input().split(' ')))
point_arr = [100,100,200,200,300,300,400,400,500]
# arr = [1001,0,0,0,0,0,0,0,0]
hacker = False
for i in range(9):
    if arr[i] >point_arr[i]:
        hacker = True

if hacker:
    print('hacker')
else:
    tp = sum(arr)
    if tp >=100:
        print('draw')
    else:
        print('none')


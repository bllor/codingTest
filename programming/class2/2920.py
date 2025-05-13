arr=[None]*8 
arr=list(input().split(' '))
mixed_arr = ''.join(arr)
if mixed_arr=='12345678':
    print('ascending')
elif mixed_arr=='87654321':
    print('descending')
else:
    print('mixed')

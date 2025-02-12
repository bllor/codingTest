from typing import MutableSequence

def shell_sort(a:MutableSequence)->None:
    n = len(a)
    h = n//2
    while h>0:
        for i in range(h,n):
            j = i - h
            print(f'{j} = {i} - {h}')
            print(f'tmp = {a[i]}')
            tmp = a[i]
            while j >=0 and a[j]>tmp:
                a[j+h]=a[j]
                print(f'a[{j+h}]=a[{j}]')
                j -=h
                print(f'{j}-={h}')
            a[j+h]=tmp
            print(f'a[{j+h}]={tmp}')
            print('a',a)
        h//=2
        
a=[8,1,4,2,7,6,3,5]
shell_sort(a)
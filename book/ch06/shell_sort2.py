from typing import MutableSequence

def shell_sort2(a:MutableSequence)->None:
    n = len(a)
    h = 1
    while h<n //9: #h의 초기값이 너무 크면 정렬하는 효과가 없다.
        h = h*3+1
        
    while h>0:
        for i in range(h,n):
            j = i -h
            tmp = a[i]
            while j>=0 and a[j]>tmp:
                a[j+h] = a[j]
                j-=h
            a[j+h]=tmp
        h//=3


    
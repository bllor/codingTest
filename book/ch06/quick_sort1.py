from typing import MutableSequence

def qsort(a:MutableSequence, left:int, right:int)->None:
    
    pl = left
    pr = right
    x = a[(left+right)//2]
    
    while pl <= pr:
        while a[pl]<x: pl+=1
        while a[pr]>x: pr-=1
        
        if pl <= pr:
            a[pl],a[pr]= a[pr],a[pl]
            pl+=1
            pr-=1
    
    if left < pr: qsort(a,left,pr)
    if pl < right: qsort(a, pl, right)

def quick_sort (a:MutableSequence)->None:
    qsort(a,0,len(a)-1)
    
if __name__ =='__main__':
    x=[5,8,4,2,6,1,3,9,7]
    
    quick_sort(x)
    
    for i in range(len(x)):
        print(x[i], end=' ')    
        
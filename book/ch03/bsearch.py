from typing import Any, Sequence

def bin_search(a: Sequence, key: Any)->int:
    pl = 0
    pr = len(a)-1
    
    while True:
        pc = (pl+pr)//2
        print(pl,pc,pr)
        if a[pc]==key:
            return pc
        elif a[pc]<key:
             pl=pc+1
        else:
            pr = pc-1
        
        if pl>pr:
            break
    return -1
    
a=[1,2,3,4,5]
key= 6

print(bin_search(a,key))
from typing import Sequence, MutableSequence

def merge_sorted_list(a:Sequence,b:Sequence,c:MutableSequence)->None:
    pa,pb,pc = 0,0,0 #각 배열의 커서(인덱스 번호)
    na,nb,nc = len(a),len(b),len(c)
    while pa <na and pb< nb:
        if a[pa]<=b[pb]:
            c[pc]=a[pa]
            pa+=1
        else:
            c[pc]=b[pb]
            pb+=1
        pc+=1
        
    while pa < na:
        c[pc]=a[pa]
        pa+=1
        pc+=1
    
    while pb<nb:
        c[pc]=b[pb]
        pb+=1
        pc+=1
    
if __name__ =='__main__':
    a=[2,4,6,8,11,13]
    b=[1,2,3,4,9,16,21]
    c = [None]*(len(a)+len(b))
    
    merge_sorted_list(a,b,c)
    print(f'c: {c}')
    
    
    
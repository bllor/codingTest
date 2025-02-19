'''
병합정렬 : 정렬을 마친 배열의 병합을 이용하여 분할 정복법에 따라 정렬하는 알고리즘
순서
1.배열의 앞부분을 병합 정렬로 정렬한다.
2.배열의 뒷부분을 병합 정렬로 정렬한다.
3.배열의 앞부분과 뒷부분을 병합한다.
'''


from typing import MutableSequence

def merge_sort(a:MutableSequence)->None:
    
    def _merge_sort(a:MutableSequence, left:int, right:int)-> None:
        print(f' _merge_sort(a:MutableSequence, left:{left}, right:{right})')
        if left < right:
            center = (left+right)//2
            print(f'center={center} = ({left}+{right})//2')
            _merge_sort(a,left,center)
            _merge_sort(a,center+1,right)
            
            
            p=j=0
            i=k=left
            
            print(f'p=j=0 {p}={j}=0')
            print(f'i=k=left {i}={k}={left}')            
            while i <= center:
                buff[p]=a[i]
                p+=1
                i +=1
            
            while i <= right and j <p:
                if buff[j]<=a[i]:
                    a[k]=buff[j]
                    j +=1
                else:
                    a[k]=a[i]
                    i+=1
                k+=1
            
            while j<p:
                a[k]= buff[j]    
                k+=1
                j+=1
    
    n = len(a)
    buff = [None]*n
    _merge_sort(a,0,n-1)
    del buff


a=[1,4,2,5,3,6]
num=len(a)
merge_sort(a)

for i in range(num):
    print(f'a[{i}]={a[i]}')
            
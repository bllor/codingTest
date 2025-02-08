from typing import MutableSequence

def shaker_sort(a:MutableSequence)-> None:
    left = 0
    right = len(a)-1
    last = right
    print(a)
    while left<right:
        for j in range(right,left,-1):
            if a[j -1]>a[j]:
                a[j-1],a[j]=a[j],a[j-1]
                last = j
        left = last
        
        for j in range(left,right):
            if a[j] > a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                last = j
        right = last


if __name__=='__main__':
    print('버블정렬')
    x = [6,4,3,7,1,9,8]
    
    shaker_sort(x)
    print('오름차순으로 정렬하였습니다.')
    for i in range(len(x)):
        print(f'x[{i}] =  {x[i]}')
    
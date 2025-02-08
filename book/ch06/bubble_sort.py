from typing import MutableSequence

def bubble_sort(a:MutableSequence)->None:
    ccnt = 0
    scnt = 0
    n = len(a)
    for i in range(n-1):
        print(f'패스 {i+1}')
        for j in range(n-1,i,-1):
            for m in range(0,n-1):
                print(f'{a[m]:2}' + (' ') if m !=j-1 else ' +' if a[j-1] > a[j] else ('- '),end='')
            print(f'{a[n-1]:2}')
            ccnt+=1
            if a[j-1]>a[j]:
                scnt+=1
                a[j-1], a[j] = a[j],a[j-1]
            
        for m in range(0,n-1):
            print(f'{a[m]:2}',end=' ')
        print(f'{a[m]:2}',end=' ')
    print(f'비교를 {ccnt}번 했습니다.')
    print(f'교환을 {scnt}번 했습니다.')
if __name__=='__main__':
    print('버블정렬')
    x = [6,4,3,7,1,9,8]
    
    bubble_sort(x)
    print('오름차순으로 정렬하였습니다.')
    for i in range(len(x)):
        print(f'x[{i}] =  {x[i]}')
    
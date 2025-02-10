from typing import MutableSequence
'''
단순 삽입 정렬 : 주목한 원소보다 더 앞쪽에서 알맞은 위치로 삽입하며 정렬하는 알고리즘
단순 선택 정렬과 비슷해 보이지마나 값이 가장 작은 원소를 선택하지 않는다는 점이 다르다.

'''
def insertion_sort(a:MutableSequence)->None:
    n = len(a)
    for i in range(1,n):
        j= i
        tmp = a[i]
        while j > 0 and a[j-1]>tmp:
            print(f'a[{j}] = a[{j-1}]')
            a[j] = a[j-1]
            j-=1
        print(f'a[{j}]={tmp}')    
        a[j]=tmp
        

if __name__=='__main__':
    print('단순삽입정렬')
    x = [6,4,3,7,1]
    insertion_sort(x)
    for i in range (len(x)):
        print(x[i], end=' ')
        
    
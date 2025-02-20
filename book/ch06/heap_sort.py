'''
힙정렬 알고리즘: 부모의 값이 항상 자식보다 크다는 힙의 특성을 이용하여 정렬한 알고리즘
(부모보다 자식이 항상큰 것도 힙인데, 일관성을 보여야 한다.)
힙은 형제의 대소관계가 정해져 있지 않으므로 부분순서트리이다.

힙정렬은 
1.힙에서 최대값을 꺼낸 뒤 
2.마지막 원소(가장 하단의 오른쪽에 위치한 원소)를 루트로 이동
3.루트에서 시작하여 자리를 교체하며 내려온다
순서로 실행이 된다.

배열을 힙으로 만드는 방법은
가장 아랫부분의 서브트리부터 상향식으로 진행하여 전체 배열을 힙으로 만든다.
'''
from typing import MutableSequence

def heap_sort(a:MutableSequence)->None:
    
    def down_heap(a:MutableSequence, left:int, right:int)->None:
        temp= a[left]
        
        parent = left
        while parent< (right+1)//2:
            cl = parent*2+1 #왼쪽 자식
            cr =cl+1 #오른쪽 자식
            child = cr if cr<=right and a[cr]>a[cl] else cl
            if temp >= a[child]:
                break
            
            a[parent] = a[child]
            parent= child
        a[parent]=temp
    
    n = len(a)
    
    for i in range((n-1)//2,-1,-1):
        down_heap(a,i,n-1) # a[i]~a[n-1]을 힙으로 만들기
    
    for i in range(n-1, 0, -1):
        a[0] ,a[i]= a[i],a[0] #최대값인 a[0]과 마지막원소를 교환
        down_heap(a,0,i-1) # a[0]~a[i-1]을 힙으로 만들기
    
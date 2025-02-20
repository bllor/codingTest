'''
도수정렬: 원소의 대소 관계를 판단하지 않고 빠르게 정렬하는 알고리즘
분포수 세기 정렬이라고도 합니다.

*
도수 분포표: 자료를 몇 개의 등급으로 나누고 각 등급에 속하는 도수를 조사하여 나타낸 표
'''

from typing import MutableSequence

def fsort(a:MutableSequence, max:int)->None:
    
    n = len(a)
    f = [0]*(max+1)
    b = [0]*n
    
    for i in range(n): f[a[i]]+=1
    for i in range(1,max+1): f[i]+=f[i-1]
    for i in range(n-1,-1,-1): f[a[i]] -=1; b[f[a[i]]]=a[i]
    for i in range(n): a[i]=b[i]
    
def counting_sort(a:MutableSequence)->None:
    
    fsort(a,max(a))
    
a=[1,5,2,4]
counting_sort(a)
print(a)
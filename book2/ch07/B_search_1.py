#재귀 함수로 구현한 이진 탐색 소스코드

def binary_search(array, target, start,end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid]==target:
        return mid
    elif array[mid]>target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)

n= 10 # 원소의 개수
target =7 #찾으려는 수
array = [1,3,5,7,9,11,13,15,17,19] #전체 원소

result = binary_search(array,target,0,n-1)
if result==None:
    print('원소없다')
else:
    print(f'{result+1}번에 위치 합니다.')
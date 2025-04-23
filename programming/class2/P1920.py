def dividArr(arr:any,n1:int,left:int,right:int):
    if left>right:
        return False
    center = (left + right) // 2
    mid = arr[center]
    if n1 ==mid:
        return True
    
    if n1 > mid:
        return dividArr(arr, n1, center+1, right)  # ✅ return 추가
    else:
        return dividArr(arr, n1, left, center-1)   # ✅ return 추가
    
# print(dividArr(arr1,0,2,len(arr1) - 1))

import sys
N = int(input())
arr1=[None]*N

arr1 = sys.stdin.readline().rstrip().split(' ')
arr1.sort()
M = int(input())
arr2=[None]*M
arr2 = sys.stdin.readline().rstrip().split(' ')
# arr2.sort()

#불필요한 2중for문을 없에고, 바로 출력을 하는 방법으로 변경
for num in arr2:
    if dividArr(arr1,num,0,N-1):
        print(1)
    else:
        print(0)



'''
이전에 제출한 코드로 시간 초과가 났음

def dividArr(arr:any,n1:int,left:int,right:int):
    if left>right:
        return False
    center = (left + right) // 2
    mid = arr[center]
    if n1 ==mid:
        return True
    
    if n1 > mid:
        return dividArr(arr, n1, center+1, right)  # ✅ return 추가
    else:
        return dividArr(arr, n1, left, center-1)   # ✅ return 추가
    
# print(dividArr(arr1,0,2,len(arr1) - 1))

import sys
N = int(input())
arr1=[None]*N

arr1 = sys.stdin.readline().rstrip().split(' ')
arr1.sort()
M = int(input())
arr2=[None]*M
arr2 = sys.stdin.readline().rstrip().split(' ')
# arr2.sort()

arr3 = [False]*M
for i in range(M):
    for j in range(N):
        arr3[i]=dividArr(arr1,arr2[i],0,N-1)
        # if arr2[i] == arr1[j]:
        #     print(1)
        #     arr3[i]=True
        #     break
        # else:
        #     arr3[i] = False

# print(arr3)
for i in range(M):
    if arr3[i]:
        print(1)
    else:
        print(0)
'''        
        
'''
  [Previous line repeated 996 more times]
RecursionError: maximum recursion depth exceeded
재귀함수가 계속 호출될 때 발생하는 오류
'''        


'''
지피티는 set을 이용하는 것이 좋을 것 같다고 하는데
set은 중복 없이 데이터를 저장하고, 빠르게 특정값을 확인할 수 있는 자료구조
in, not in 연산이 아주 빠름

'''
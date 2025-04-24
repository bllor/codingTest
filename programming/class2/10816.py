


'''
이진탐색을 한 다음 같은 숫자를 세기 위해서 for문을 사용했는데,
이 부분에서 시간이 오래 걸려서 실패하게 되었음

import sys
N = int(input())
arr1 = list(map(int,sys.stdin.readline().split(' ')))
arr1.sort()
M = int(input())
arr2 = list(map(int,sys.stdin.readline().split(' ')))
arr3 = [0]*M
def dividArr(arr:any, t:int, s:int, e: int,arrno:int):
    if s>e:
        return 0
    midNo = (s+e)//2
    mid = arr[midNo]
    if t == mid:
        tn=0
        for i in range(midNo,e+1):
            if t== arr[i]:
                tn+=1
            else:
                break
        for i in range(midNo-1,-1,-1):
            if t== arr[i]:
                tn+=1
            else:
                break
        arr3[arrno]=tn
    elif t>mid:
        return dividArr(arr,t,midNo+1,e,arrno)
    else:
        return dividArr(arr,t,s,midNo-1,arrno)
        
    
for i in range(M):
    dividArr(arr1,int(arr2[i]),0,N-1,i)

# for i in arr3:
#     print(i, end=' ')
print(' '.join(map(str, arr3)))

'''
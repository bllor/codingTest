import sys

# 입력
N = int(input())
arr1 = list(map(int, sys.stdin.readline().split()))
arr1.sort()

M = int(input())
arr2 = list(map(int, sys.stdin.readline().split()))
arr3 = [0] * M

# 이진 탐색 - 직접 구현한 lower_bound
def lower_bound(arr, target):
    s, e = 0, len(arr)
    while s < e:
        m = (s + e) // 2
        if arr[m] < target:
            s = m + 1
        else:
            e = m
    return s

# 이진 탐색 - 직접 구현한 upper_bound
def upper_bound(arr, target):
    s, e = 0, len(arr)
    while s < e:
        m = (s + e) // 2
        if arr[m] <= target:
            s = m + 1
        else:
            e = m
    return s

# 함수 이름은 살림
def dividArr(arr, t, arrno):
    lo = lower_bound(arr, t)
    hi = upper_bound(arr, t)
    arr3[arrno] = hi - lo

# 탐색
for i in range(M):
    dividArr(arr1, arr2[i], i)

# 출력
print(' '.join(map(str, arr3)))

'''
ex)배열이 [2,2,2,2,3]이고 찾는 숫자가 2일 때
[1]lower_bound
1)
s,e = 0,4
m = 2
arr[m]<2 --> false
e = 2
2)
s,e = 0,2
m = 1  
arr[m]<2 --> false
e = 1
3)
s,e = 0,1
m = 0
arr[m]<2 --> false
e = 0
4)
s,e = 0,0
false
s = 0

[2]upper_bound
1)
s,e = 0,4
m = 2
arr[2]<=2 --> true
s = 3
2)
s,e = 3,4
m = 3  
arr[3]<=2 --> true
e = 1
s = 4
3)
s,e = 4,4
false
return s = 4

2 = 4-0 = 4개
'''
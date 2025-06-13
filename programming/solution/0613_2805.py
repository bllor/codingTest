import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def binary_search(arr, st, fi, target):
    result = 0
    while st <= fi:
        mid = (st + fi) // 2
        total = sum([i - mid for i in arr if i > mid])
        if total >= target:
            result = mid  # 조건을 만족했으므로 저장하고 더 높게 시도
            st = mid + 1
        else:
            fi = mid - 1
    return result

print(binary_search(arr, 0, max(arr), M))

'''
내 코드는 나무의 길이와 잘랐을 때의 길이가 같을 때만 리턴해주고
잘랐을 때의 길이가 나무의 길이보다 길 경우를 커버해주지 못한다.

import sys
input = sys.stdin.readline
N,M = map(int, input().split(' '))
arr = list(map(int,input().split(' ')))
arr.sort()
mn = max(arr)
n_arr = [_ for _ in range(mn+1)]
pos_arr = []
def divide_sort(arr,st,fi,word_length):
    if st>fi:
        return fi # 가장 마지막으로 가능했던 높이
    result = 0
    mid = (st+fi)//2
    slicedLength = [i-n_arr[mid] for i in arr if i-n_arr[mid]>0]
    if word_length == sum(slicedLength):
        return n_arr[mid]
    if word_length> sum(slicedLength): 
    #너무 작게 자른 경우로, 높이를 더 낮게 시도
        return divide_sort(arr,st,mid-1,word_length)
    else:
    #조건에 만족하거나 혹은 조건보다 더 자른경우, 높이를 더 높임
        return divide_sort(arr,mid+1,fi,word_length)

print(divide_sort(arr,0,mn,M))
 
'''
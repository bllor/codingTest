import sys
input = sys.stdin.readline
# N,M  = 4,7
N,M = map(int, input().split(' '))
arr = list(map(int,input().split(' ')))
arr.sort()
mn = max(arr)
n_arr = [_ for _ in range(mn+1)]
# print(n_arr)
pos_arr = []
def divide_sort(arr,st,fi,word_length):
    if st>fi:
        return 'none'
    result = 0
    mid = (st+fi)//2
    # print('-',n_arr[mid])
    slicedLength = [i-n_arr[mid] for i in arr if i-n_arr[mid]>0]
    # print('sl',sum(slicedLength),slicedLength)
    if word_length == sum(slicedLength):
        return n_arr[mid]
    if word_length> sum(slicedLength):
        pos_arr.append(n_arr[mid])
        return divide_sort(arr,st,mid-1,word_length)
    else:
        return divide_sort(arr,mid+1,fi,word_length)

print(divide_sort(arr,0,mn,M))

    
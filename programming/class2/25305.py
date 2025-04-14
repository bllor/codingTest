n, p = map(int,input().split(' '))

arr =[None]*n
arr = list(map(int, input().split(' ')))
arr.sort()
print(arr[n-p])

# n,p = 5,2
# arr = [100,76,85,93,98]
# print(arr)
# print(arr)
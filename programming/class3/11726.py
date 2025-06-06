import sys
input = sys.stdin.readline().rstrip()

N = int(input)
arr = [0]*N

for i in range(N):
    if i==0:
        arr[i]=1
    elif i==1:
        arr[i] = 2
    else:
        arr[i] = arr[i-1]+arr[i-2]

# print(arr)
print(arr[N-1]%10007)

'''
1 1
2 11 2
3 111 12 21
4 1111 211 121 112 22

'''

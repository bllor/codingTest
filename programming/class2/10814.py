N = int(input())

arr = [None]*N
for i in range(N):
    age,name= input().split(' ')
    arr[i]=[int(age),i,name]

arr.sort()
for i in range(N):
    print (arr[i][0],arr[i][2])
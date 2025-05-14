n,m = map(int, input().split(' '))

arr = [None]*n
for i in range(n):
    arr[i] = [input(),i]

arr.sort()
s_arr = [None]*m

for j in range(m):
    s_arr[j]=input()
n_arr = ['1','2','3','4','5','6','7','8','9']
for s in s_arr:
    if s[0] in n_arr:
        print(arr[int(s)-1][0])
    else:
        for i in range(len(arr)):
            if arr[i] == s:
                print(arr[int(s)-1][0][1])

import sys
N = int(input())
value= sys.stdin.readline().rstrip()
arr = value.split(' ')
maxLength = 1

for i in range(len(arr)):
    i_arr = set()
    i_arr.add(arr[i])
    mm=1
    for j in range(i+1,N):
        i_arr.add(arr[j])
        # print(i_arr,mm)
        if len(i_arr)>2:
            if mm>maxLength:
                # print(mm,maxLength)
                maxLength=mm
            mm=1
            break
        mm+=1
    if mm>maxLength:
        # print(mm,maxLength)
        maxLength=mm
print(maxLength)
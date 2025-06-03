import sys
N = int(input())
arr = [None]*N
for i in range(N):
    arr[i] = int(sys.stdin.readline().rstrip())

# N = 6
# i_arr = '10 20 30 40 50 60'
# i_arr2 = '10 20 15 25 10 20'
# arr = list(map(int, i_arr2.split(' ')))
s_arr = [True]*N
ss=2
tn = arr[N-1]
for i in range(N-1,0,-1):
    # print(i,i-1,i-2)
    if ss==3:
        # print('ss')
        ss=1
        continue
    if i ==1:
        tn+=arr[0]
    else:
        if s_arr[i]:
            if arr[i-1]>arr[i-2]:
                # print('i-1',arr[i-1])
                tn+=arr[i-1]
                ss+=1
            else:
                tn+=arr[i-2]
                # print('i-2',arr[i-2])
                s_arr[i-1]=False
                ss=1
        else:
            ss=1
print(tn)
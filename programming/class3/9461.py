arr=[0]*101
for i in range(101):
    if i==0 or i ==1 or i ==2:
        arr[i] = 1
    else:
        arr[i] = arr[i-3]+arr[i-2]
        
N = int(input())
i_arr = [None]*N
for i in range(N):
    n = int(input())
    i_arr[i] = f'{arr[n-1]}'
            
print('\n'.join(i_arr))
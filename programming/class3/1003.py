'''
0 > 1 0
1 > 0 1
2
0 1
3
2 1
0 1 1> 1 2 
'''
z_arr = [None]*41
o_arr = [None]*41
TN = int(input())
for i in range(TN):
    N = int(input()) 
    for i in range(N+1):
        if i-2 <0:
            if i ==1:
                o_no=1
                z_arr[i]=0
                o_arr[i]=1
            else:
                z_no=1
                z_arr[i]=1
                o_arr[i]=0
        else:
            zno = z_arr[i-1]+z_arr[i-2]
            ono = o_arr[i-1]+o_arr[i-2]
            z_arr[i] = zno
            o_arr[i] = ono
    print(z_arr[N],o_arr[N])
    
        
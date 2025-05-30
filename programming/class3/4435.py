g_arr= [1,2,3,3,4,10]
s_arr = [1,2,2,2,3,5,10]


N = int(input())
i_arr=[None]*N
i_arr2=[None]*N

for i in range(N):
    i_arr[i] = input()
    i_arr2[i] = input()


for no in range(N):
    i_s = list(map(int, i_arr[no].split(' ')))
    i_s2 = list(map(int, i_arr2[no].split(' ')))

    for i in range(len(g_arr)):
        g_arr[i] = g_arr[i]*i_s[i]
    
    for j in range(len(s_arr)):
        s_arr[j] = s_arr[j]*i_s2[j]
    
    print(f'Battle {no+1}: ',end='')
    # print(sum(g_arr),sum(s_arr))
    if sum(g_arr)> sum(s_arr):
        print('Good triumphs over Evil')
    elif sum(g_arr)< sum(s_arr):
        print('Evil eradicates all trace of Good')
    else:
        print('No victor on this battle field')
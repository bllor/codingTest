'''
3,1,4,3,2
3 4 8 11 13 --> 39

1 2 3 3 4
1 3 6 9 13

'''
import sys
N = int(input())
i_arr = list(map(int, sys.stdin.readline().rstrip().split(' ')))
p_arr = [None]*N

i_arr.sort()
for i in range(N):
    if i ==0:
        p_arr[i]= i_arr[i]
    else:
        p_arr[i] = p_arr[i-1]+i_arr[i]
print(sum(p_arr))
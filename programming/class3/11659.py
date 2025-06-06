import sys
N,M = map(int,sys.stdin.readline().rstrip().split(' '))
arr = list(map(int,sys.stdin.readline().rstrip().split(' ')))

# N,M = 5,3
# arr = list(map(int,'5 4 3 2 1'.split(' ')))
# print(sum(arr[0:2]))
# p_arr= []
for i in range(M):
    s,t = map(int,sys.stdin.readline().rstrip().split(' '))
    print(sum(arr[s-1:t]))
    # p_arr.append(f'{sum(arr[s-1:t])}')

# print('\n'.join(p_arr))
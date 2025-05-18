from collections import deque 
import sys
N = int(input())
dq = deque()


def str_sort(x):
    if 'push' in x:
        s1 = x.split(' ')[1]
        dq.append(s1)
    if 'front' in x:
        if len(dq)==0:
            print('-1')
        else:
            print(f'{dq[0]}')
    if 'pop' in x:
        if len(dq)==0:
            print('-1')
        else:
            print(f'{dq.popleft()}')
    if 'size' in x:
        print(f'{len(dq)}')
    
    if 'empty' in x:
        if len(dq)==0:
            print('1')
        else:
            print('0')
    if 'back' in x:
        if len(dq)==0:
            print('-1')
        else:
            print(f'{dq[len(dq)-1]}')        
        
i_arr  =[None]*N
for i in range(N):
    input_str  = sys.stdin.readline().rstrip()
    # input_str = input()
    # print(input_str)
    # print(type(input_str))
    i_arr[i]=input_str

for ip in i_arr:
    str_sort(ip)

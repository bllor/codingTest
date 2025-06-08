# a= 'aa'
# if  a[0] in ['1','2','3','4','5']:
#     print('t')
# else:
#     print('f')

import sys
inputs = sys.stdin.readline().rstrip()
n,s  =  inputs.split(' ')

no_arr = [None]*int(n)
name_arr = []

for i in range(int(n)):
    value = input()
    no_arr[i]  = i
    name_arr.append(value)
# print(no_arr)
# print(name_arr)
for j in range(int(s)):
    value = input()
    if  value[0] in ['1','2','3','4','5','6','7','8','9']:
        print(name_arr[int(value)-1])
    else:
        print(name_arr.index(value)+1)
        # print('f')
    
'''
4 4 1
1234
4 5 4
1234 1235 1345
2345
4 6
1234 1235 1345 1236 1245 1246 1346 1456
2345 2346 2456
3456

4 7 20
1234 1235 1236 1237 
'''

N,M = 13,29
arr = [0]*(M+1)
arr[1] = 1
arr[2] = N
print(len(arr))
for i in range(3,len(arr)):
    print(i,arr[i-1])
    arr[i] = arr[i-1]+N*(i-2)
print(arr[29])

# T = 3
# for i in range(T):
#     N,M = map(int, input().split(' '))
#     if N ==1:
#         print(M)
#     elif N==0:
#         print(0)
#     else:
#         arr=[0]*(N+1)
        
def divide_search(arr,st,fi,target):
    # print(st,fi)
    if st>fi:
        return 0
    mid = (st+fi)//2
    # print('mid',mid)
    if arr[mid]==target:
        return mid

    if arr[mid]>target:
    #    print('mid>')
       return divide_search(arr,st,mid-1,target)
    else:
    #    print('mid<')
       return divide_search(arr,mid+1,fi,target)
    
import sys
N,M = map(int, sys.stdin.readline().rstrip().split(' '))
n_arr = [None]*N
m_arr = [None]*M

for i in range(N):
    i_name = sys.stdin.readline().rstrip()
    n_arr[i] = i_name
    
for i in range(M):
    i_name = sys.stdin.readline().rstrip()
    m_arr[i] = i_name

nm_arr = []

n_arr.sort()
m_arr.sort()

for i in range(N):
    n_name = n_arr[i]
    s_name = m_arr[divide_search(m_arr,0,len(m_arr)-1,n_name)]
    if n_name == s_name:
        nm_arr.append(n_name)
print(len(nm_arr))
print('\n'.join(nm_arr))            
# # # if N>M:
# # #     for m in m_arr:
# # #         for n in n_arr:
# # #             if n==m:
# # #                 nm_arr.append(m)
# # # else:
# # #     for n in n_arr:
# # #         for m in m_arr:
# # #             if n==m:
# # #                 nm_arr.append(m)

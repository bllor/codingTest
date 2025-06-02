import sys
def divide_search(arr,st,fi,target):
    if st>fi:
        return 
    mid = (st+fi)//2
    if arr[mid][0] == target:
        return mid
    if arr[mid][0] > target:
        return divide_search(arr,st,mid-1,target)
    else:
        return divide_search(arr,mid+1,fi,target)
    

N,M = map(int, sys.stdin.readline().rstrip().split(' '))

s_arr=[None]*N
p_arr=[None]*N
for i in range(N):
    site,pw = sys.stdin.readline().rstrip().split(' ')
    s_arr[i]=[site, i]
    p_arr[i]=pw


s_arr.sort()
solve_arr = []
for j in range(M):
    search_site= sys.stdin.readline().rstrip()
    s_no = s_arr[divide_search(s_arr,0,N-1,search_site)][1]
    solve_arr.append(p_arr[s_no])    

print('\n'.join(solve_arr))        
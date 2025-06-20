import sys
input = sys.stdin.readline
# N,M = map(int, input().split(' '))
N,M = 6,5
arr = []
for i in range(N+1):
    arr.append([])
i_arr = [
'1 2',
'2 5',
'5 1',
'3 4',
'4 6',
]
tf_arr= [True]

for i in range(N):
    tf_arr.append(False)
for i in range(M):
    a,b = map(int,i_arr[i].split(' '))
    arr[a].append(b)
    arr[b].append(a)
    arr[a].sort()
    arr[b].sort()
print(arr)

cc = 0
print(tf_arr)
def conn(N):
    print('conn',N,arr[N])
    tf_arr[N] = True
    for i in arr[N]:
        print(i)
        if not tf_arr[i]:
            return conn(N)        
conn(1)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)#이걸 해주지 않으면 RecursionError가 발생한다.

N,M = map(int, input().split(' '))
arr = []
for i in range(N+1):
    arr.append([])
tf_arr = [False] * (N + 1)

for i in range(M):
    a,b = map(int,input().split(' '))
    arr[a].append(b)
    arr[b].append(a)
    arr[a].sort()
    arr[b].sort()

cc = 0
def conn(N):
    tf_arr[N] = True
    for i in arr[N]:
        if not tf_arr[i]:
            conn(i)
                   

# 연결 요소 세기
count = 0
for i in range(1, N+1):
    if not tf_arr[i]:
        conn(i)
        count += 1

print(count) 

'''
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

dfs로 탐색하기 위해서 코드를 작성하려고 했는데 코드에서 실수가 있었음
if not tf_arr[i]:
            return conn(N)  
자기 자신을 재귀호출하고 있고, return을 하여 함수를 끝내게 만듬
conn(i)만 작성하여 연결된 노드 i로 재귀적으로 탐색하게 수정

연결 요소를 세기 위해서 한번도 방문하지 않은 정점을 기준으로 DFS를 실행하고 연결 요소 개수를 증가시킨다

'''
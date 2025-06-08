N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]	

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)				# 양방향
visited = [False] * (N+1)
count = -1
print(graph)
def DFS(v):
    visited[v] = True
    global count
    count += 1
    for i in graph[v]:
        if not visited[i]:
            DFS(i)

DFS(1)
print(count)
'''
접근 조차할 수 없었음
그래프 문제 공부 필요

접근을 할 수 없었던 문제로 풀이를 통해 복기하려 한다.
컴퓨터의 수 : 7대
연결된 컴퓨터 쌍의 개수: 6개
연결된 컴퓨터 번호쌍
arr= [
'1 2',
'2 3',
'1 5',
'5 2',
'5 6',
'4 7',
]	
graph = [[] for _ in range(N+1)]	

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)	
graph에 저장된 배열
[[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
1번은 2,5번 2번은 1,3,5번 3번은 2, 4번은 7, 5번은 1,2,6번 6번은 5, 7번은 4와 연결되어있음을 알 수 있다.

visited = [False] * (N+1)
count = -1
def DFS(v):
    visited[v] = True
    global count
    count += 1
    for i in graph[v]:
        if not visited[i]:
            DFS(i)

DFS(1)
print(count)

dfs에 1이 들어갈 경우
visited[1]= true
count는 1이 올라가서 0이 된다.
for i in graph[1]:
    2번 5번 방문
    1) i==2
        dfs(2)
        --> count+=1
            1,3,5번 방문해야 하지만 1번은 true이므로 3,5번 방문
            1-1) i==3
                count+=1
                2번 -true
            1-2) i==5
                1,2,6번 중 6번 방문
                    1-2-1) i==6
                        count+=1
                        5번 방문해야 하지만 true라 패스
    2)5번
    트루라 패스

count는 4가 된다.

            
            
'''
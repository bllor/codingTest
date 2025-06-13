from collections import deque

def dfs(n):
    print(n, end=' ')
    visited[n] = True

    for i in graph[n]:
        if not visited[i]:
            dfs(i)


def bfs(n):
    visited[n] = True
    queue = deque([n])

    while queue:
        q = queue.popleft()
        print(q, end=' ')

        for i in graph[q]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


# main
n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

print(graph)
# 정점 번호가 작은 것이 먼저 오도록 정렬
for i in range(n + 1):
    graph[i].sort()

# 출력
visited = [False] * (n + 1)
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)

'''
문제를 푸는 방법을 몰라서 풀이를 적는 것으로 대체

이 문제는 그래프 문제로 인접 리스트를 구하고, 정점 번호가 작은 것을 먼저 방문하기 위해 정렬을 한다.

정점의 개수: 4 
간선의 개수: 5
탐색을 시작할 정점의 번호: 1
간선 정보(input()에 들어갈 값): 1 2, 1 3, 1 4, 2 4, 3 4 
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
print(graph) --> [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]

for g in graph:
    g.sort()
    #정렬하는 이유는 정점 번호가 작은 것부터 방문하기 위해서 정렬함


# 출력
1.dfs
visited = [False] * (n + 1)
dfs(v)
def dfs(n):
    print(n, end=' ')
    visited[n] = True

    for i in graph[n]:
        if not visited[i]:
            dfs(i)
1)v=1
print(1)
visited[n] = True -->visited = [False,True,False,False,False]
for i in graph[n]:
    i = 2,3,4
    if not visited[i]:
        dfs(i)
        2가 가장 먼저 있으므로 2부터 실시
    1-1)v = 2
    print(2)
    visited[2] = True -->visited = [False,True,True,False,False]
    for i in graph[n]:
        i = 1,4
        visited[1]은 true이므로 패스,
        if not visited[i]:
            dfs(i)
            dfs(4)
        1-1-1)v = 4
        print(2)
        visited[4] = True -->visited = [False,True,True,False,True]
        for i in graph[n]:
            i = 1,2,3
            visited[1],visited[2]은 true이므로 패스,
            if not visited[i]:
                dfs(i)
                dfs(3)
            1-1-1-1)v = 3
            print(3)
            visited[3] = True -->visited = [False,True,True,True,True]
            for i in graph[n]:
                i = 1,4
                visited[1],visited[4]은 true이므로 패스
    1-2)i=3
        visited[3] = True이므로 패스
    
    1-3)i=4
        visited[4] = True이므로 패스

2.bfs
visited = [False] * (n + 1)
bfs(v)
def bfs(n):
    visited[n] = True
    queue = deque([n])

    while queue:
        q = queue.popleft()
        print(q, end=' ')

        for i in graph[q]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
1. n=1
    visited[n] = True -->visited = [False,True,False,False,False]
    queue = [1]
    while queue:
        q = queue.popleft()--> queue = []
        print(1)
        for i in graph[1]:
            i = 2,3,4
            1) i= 2
            2는 not visited
                visited = True
                queue.append(2)
            1) i= 3
            3는 not visited
                visited = True
                queue.append(3)
            1) i= 4
            4는 not visited
                visited = True
                queue.append(4) -->queue = [2,3,4]
    while queue:
        q = queue.popleft()--> queue = [3,4]
        print(2)
        for i in graph[2]:
            i = 1,4
            visited[1],visited[4] True
    
    while queue:
        q = queue.popleft()--> queue = [4]
        print(3)
        for i in graph[3]:
            i = 1,4
            visited[1],visited[4] True
   
   while queue:
        q = queue.popleft()--> queue = []
        print(4)
        for i in graph[4]:
            i = 1,2,3
            visited[1],visited[2],visited[3] True
    
     
        
'''

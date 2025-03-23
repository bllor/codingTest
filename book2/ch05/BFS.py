from collections import deque

'''
BFS(Breadth First Search)
가까운 노드부터 탐색하는 알고리즘
bfs구현에서는 선입선출 방식인 큐 자료구조를 이용하는 것이 정석이다.
[1]동작 방식
1)탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다
2)큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노들 모두 큐에 삽입하고 방문처리를 한다
3)2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.
'''

#def 메서드 정의
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start]=True
    
    #큐가 빌 때까지 반복
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]    
]

visited = [False]*9

bfs(graph,1,visited)
import sys
input = sys.stdin.readline
INF = int(1e9)

#노드의 개수, 간선의 개수를 입력받기
n, m = 6, 11
#시작 노드 번호 입력받기
start = 1
#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
#방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False]*(n+1)
#최단 거리 테이블을 모두 무한으로 초기화
distance = [INF]*(n+1)

arr = [(1,2,2),(1,3,5),(1,4,1),(2,3,3),(2,4,2),(3,2,3),(3,6,5),(4,3,3),(4,5,1),(5,3,1),(5,6,2)]

#모든 간선 정보를 입력 받기
for i in range(len(arr)):
    a,b,c = arr[i][0],arr[i][1],arr[i][2]
    # a번에서 b번으로 가는 비용이 c라는 의미
    graph[a].append((b,c))


def get_smalllest_node():
    min_value = INF
    index = 0
    for i in range(1,n+1):
        if distance[i]< min_value and  not visited[i]:
            min_value = distance[i]
            index=i
    return index

def dijkstra(start):
    #시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    #시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        now  = get_smalllest_node()
        visited[now] = True
        
        for j in graph[now]:
            cost = distance[now]+j[1]
            if cost <distance[j[0]]:
                distance[j[0]] = cost 

#다익스트라 알고리즘 수행
dijkstra(start)

#모든 노드로 가기 위한 최단 거리 출력

for i in range(1,n+1):
    #도달할 수 없는 경우, 도달할 수 없다고 출력
    if distance[i] == INF:
        print('도달할 수 없습니다.')
    else:
        print(f'{start}번에서 {i}번까지 최단 거리는 {distance[i]}입니다.')    
    
   

#개선된 다익스트라 알고리즘 소스코드
'''
직관적으로 봤을 때, 우선순위 큐를 이용하는 방식이 훨씬 빠른 이유를 모를 수도 있다.
우리의 코드에서 확인할 수 있듯이 한 번 처리된 노드는 더 이상 처리 되지 않는다.
다시 말해 큐에서 노드를 하나씩 꺼내 검사하는 반복문은 노드의 개수 V 이상의 횟수로 반복되지 않는다.
'''
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

#노드의 개수, 간선의 개수
n = 6
m = 11
#시작번호 입력받기
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


def dijkstra(start):
    q = []
    #시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start]= 0
    while q: #큐가 비어있지 않다면
        #가장최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        #현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] <dist:
            continue
        
        for i in graph[now]:
            cost = dist+i[1]
            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost <distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))


dijkstra(start)

for i in range(1,n+1):
    #도달할 수 없는 경우, 도달할 수 없다고 출력
    if distance[i] == INF:
        print('도달할 수 없습니다.')
    else:
        print(f'{start}번에서 {i}번까지 최단 거리는 {distance[i]}입니다.')    
     
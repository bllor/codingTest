INF = int(1e9)

#노드의 개수와 간선의 개수 입력 받기
n = 4
m = 7
#2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF]*(n+1)for _ in range(n+1)]

#자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]= 0
#입력값
arr= [
'1 2 4',
'1 4 6',
'2 1 3',
'2 3 7',
'3 1 5',
'3 4 4',
'4 3 2',
]
#각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for i in range(m):
    a,b,c = map(int, arr[i].split(' '))
    graph[a][b] = c

#점화식에 따라 플로이드 워셜 알고리즘을 수행
#min(graph[a][b],graph[a][k]+graph[k][b])은
#a에서b로 가는 비용이 a에서k로 갔다가 k에서 b로 가는 비용을 비교하여 작은 값을 저장
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1,n+1):
    for b in range(1, n+1):
        if graph[a][b]== INF:
            print('infinity', end=' ')
        else:
            print(graph[a][b], end=' ')
    print(' ')
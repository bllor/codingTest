import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# dfs 정의
def dfs(x, y):
    # 상하좌우
    print('dfs',x,y)
    dx = [0, 0, -1, 1] 
    dy = [1, -1, 0, 0]

    # 네 방향 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 안에 있고 1이면(=배추이면) 지나간것을 -1로 표시하고 주변 탐색
        if (0 <= nx < m) and (0 <= ny < n) and graph[ny][nx] == 1:
            print(nx,ny)
            graph[ny][nx] = -1
            dfs(nx, ny)

t = int(input()) # 테스트 케이스의 개수
for _ in range(t):
    m, n, k = map(int, input().split()) # 가로, 세로, 배추 개수
    graph = [[0 for _ in range(m)] for _ in range(n)]

    # 배추 위치 표시
    for _ in range(k):
        X, Y = map(int, input().split()) 
        graph[Y][X] = 1 # X, Y 바꿔서 표시해야하는거 주의!

    # 배추 그룹 수(=배추흰지렁이 개수) 세기
    count = 0
    for a in range(m):
        for b in range(n):
            if graph[b][a] == 1:
                dfs(a ,b)
                count += 1
    print(count)
'''
문제에 접근도 하지 못했음
아래와 같이 배추가 심겨져 있을 경우
[   
[1,0,0],
[1,0,0],
[0,1,1]
]
1.b=0,a=0일 때
graph[0][0] = 1
dfs(0,0)
x,y = 0,0
# 상하좌우
dx = [0, 0, -1, 1] 
dy = [1, -1, 0, 0]
for i in range(4):
1)i=0
    nx = 0
    ny = 1
    graph[1][0]은 1이므로 graph[1][0]을 -1로 변경함
    dfs(0,1)
    1-1)
        dfs(0,1)
        x,y = 0,1
        for i in range(4):
        1-1-1)i==0 
                nx = 0, ny = 2
                graph[2][0] =0     
        i==1,i==2,i==3 graph들은 다 0
2)i=1 3)i=2 4)i=3 전부 0

2.b = 2,a = 1 일 때 graph[2][1] = 1
dfs(1,2)
x,y = 1,2
for i in range(4):
1)i=0
    nx,ny  = 1,3 ny가 n과 같으므로 패스
2)i=1
    nx,ny = 1,1 graph[1][1]은 0으로 패스
2)i = 2
    nx,ny = 0,2 graph[0][2]은 0
3)i = 3
    nx,ny = 2,2 graph[2][2]는 1로, -1로 변경

graph[2][2]는 -1이 되어서 패스 된다.

    
'''
"""
여행가는 N X N 크기의 정사각형 공간 위에 서있다.
가장 왼쪽 위 좌표는 1*1이고, 가장 오른쪽 아래 좌표는 N * N이다.
우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여 있다.
계획서에는 하나의 줄에 띄워쓰기를 기준으로 하여 L,R,U,D 중 하나의 문자가 반복적으로 적혀있다.
L: 왼쪽 R:오른쪽 이동 U:위로 이동 D:아래쪽 이동
이 때 여행가가 N X N 크기의 정사각형 공간을 벗어나는 움직임은 무시된다.

입력 조건  
- 첫째 줄에 공간의 크기를 나타내는 N이 주어진다.
- 둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다.

출력 조건
- 첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표를 공백으로 구분하여 출력한다.    

"""
n = int(input())
x,y = 1,1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types= ['L','R','U','D']

for plan in plans :
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x+dx[i]
            ny = y+dy[i]
    
    if nx <1 or ny <1 or nx>n or ny >n:
        continue
    
    x,y = nx,ny

print(x,y)
            
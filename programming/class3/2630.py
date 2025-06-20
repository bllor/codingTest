def divide(row, col, size): 
    color = paper[row][col]  # 현재 영역의 색상
    for i in range(row, row + size):     # 세로 방향(행)
        for j in range(col, col + size): # 가로 방향(열)
            if paper[i][j] != color:     # 색이 다르면 분할
                half = size // 2
                divide(row, col, half)              # 2사분면 (왼쪽 위)
                divide(row, col + half, half)       # 1사분면 (오른쪽 위)
                divide(row + half, col, half)       # 3사분면 (왼쪽 아래)
                divide(row + half, col + half, half)# 4사분면 (오른쪽 아래)
                return
    # 모두 같은 색일 경우
    if color == 0:
        result[0] += 1  # 흰색
    else:
        result[1] += 1  # 파란색

import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
result = [0, 0]

divide(0, 0, N)

print(result[0], '\n', result[1], sep='')

'''
color = paper[y][x] # 색종이의 색
[y][x]로 하는 이유는
[
    [1, 2, 3],  
    [4, 5, 6],  
    [7, 8, 9],  
]
6을 고르기 위해서는 [1][2]가 되어야 함
y가 세로, x는 가로
'''

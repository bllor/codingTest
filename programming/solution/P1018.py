n, m = map(int, input().split())
board = [input() for _ in range(n)]

min_paint = float('inf')

# 체스판에서 8x8 크기의 모든 위치 순회
for i in range(n - 7):
    for j in range(m - 7):
        w_start = 0  # 왼쪽 위가 W인 경우
        b_start = 0  # 왼쪽 위가 B인 경우
        for x in range(8):
            for y in range(8):
                # 현재 칸의 색
                current = board[i + x][j + y]
                # 좌표의 짝수/홀수 여부에 따라 원래 색 결정
                if (x + y) % 2 == 0:
                    if current != 'W':
                        w_start += 1
                    if current != 'B':
                        b_start += 1
                else:
                    if current != 'B':
                        w_start += 1
                    if current != 'W':
                        b_start += 1
        min_paint = min(min_paint, w_start, b_start)

print(min_paint)
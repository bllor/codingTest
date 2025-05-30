import sys

K, N = map(int, sys.stdin.readline().split())
lines = [int(sys.stdin.readline()) for _ in range(K)]

start = 1  # 최소 길이
end = max(lines)  # 최대 길이

result = 0

while start <= end:
    mid = (start + end) // 2
    count = sum(line // mid for line in lines)

    if count >= N:
        result = mid  # 일단 저장하고
        start = mid + 1  # 더 큰 길이 탐색
    else:
        end = mid - 1  # 더 작은 길이 탐색

print(result)


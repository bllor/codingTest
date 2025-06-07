import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 1001

# 초기값 지정
dp[0] = 1
dp[1] = 1

# 점화식에 따른 경우의 수 계산
for i in range(2, n+1):
    dp[i] = dp[i-1] + 2 * dp[i-2]

print(dp[n]%10007)

'''
규칙을 찾지 못해서 풀지 못했음
1 1
2 3
3 5
4 11
1111 1
112 121 211 6
22  r22 2r2 r2r2 4

'''
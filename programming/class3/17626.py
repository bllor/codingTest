N = 25
if N%N**0.5==0:
    #제곱일 때 
    print(1)
else:
    dp = [0]*(N+1)
    dp[0] = 0
    
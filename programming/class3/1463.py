x = 10
dp = [0] * (x + 1)

for i in range(2, x + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp)


N = 10
tn=0
while N>1:
    print(N,tn)
    if N%3==2:
        if N%2==0:
            N=N//2
            tn+=1
        else:
            N=N-2
            tn+=2
    elif N%3==1:
        if N%2==0:
            print('b',N)
            N=N//2
            print('a',N)
            tn+=1
        else:
            N=N-1
            tn+=1
    else:
        N=N//3
        tn+=1
print('t',tn)
            
            
import sys
# iarr = [
# 1,
# 5,
# 10,
# 50,
# 100,
# 500,
# 1000,
# 5000,
# 10000,
# 50000,
# ]
N,K = map(int, sys.stdin.readline().rstrip().split(' '))


arr=[None]*N

for i in range(N):
    arr[i]=int(sys.stdin.readline())

cn = 0
for no in range(N-1,-1,-1):
    if (K//arr[no]):
        cn+=K//arr[no]
        K = K%arr[no]

print(cn)
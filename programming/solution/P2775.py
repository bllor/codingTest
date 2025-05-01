def personNum(k: int, n: int, memo: dict) -> int:
    if (k, n) in memo:
        return memo[(k, n)]
    
    if k == 0:
        memo[(k, n)] = n
    else:
        memo[(k, n)] = sum(personNum(k - 1, i, memo) for i in range(1, n + 1))
    
    return memo[(k, n)]

T = int(input())
arr = [None] * T

for i in range(T):
    k = int(input())
    n = int(input())
    arr[i] = [k, n]

for k, n in arr:
    memo = {}
    print(personNum(k, n, memo))
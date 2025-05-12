import sys
input = sys.stdin.readline

N, M = map(int, input().split())
is_prime = [True] * (M + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(M**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, M + 1, i):
            is_prime[j] = False

for i in range(N, M + 1):
    if is_prime[i]:
        print(i)
        
'''
나의 코드는 시간 복잡도를 해결하지 못했다.

3, 16일 때
for i in range(2,5):
    if is_prime[2]:--> true
        for j in range(4,17,2):
            is_prime[j]= False
            4,6,8,10,12,14,16 false
    if is_prime[3]-->true
        for j in range(9,17,3):
            is_prime[j]=False
            9,12,15 false
                    
'''
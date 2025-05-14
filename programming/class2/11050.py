import math
N,K = map(int, input().split(' '))

a = math.factorial(N)
b = math.factorial(N-K)*math.factorial(K)

print(a//b)

'''
이항계수란 주어진 집합에서 원하는 개수만큼 순서없이 뽑는 조합의 개수
5개 중 2개를 뽑을 때
1 2
1 3
1 4
1 5
2 3
2 4
2 5
3 4
3 5
4 5
10개이다.
'''


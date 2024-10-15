# 1부터 n까지 정수의 합 구하기

n = int(input())

i = 0
sum =0
while i<=n: # i가 n보다 크거나 같지 않을 때까지 반복
    sum+=i
    i+=1
print(sum)
    
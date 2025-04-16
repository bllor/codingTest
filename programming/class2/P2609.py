n1, n2 = map(int, input().split())

# 최대공약수 구하기
for i in range(min(n1, n2), 0, -1):
    if n1 % i == 0 and n2 % i == 0:
        gcd = i
        break

# 최소공배수는 곱해서 최대공약수로 나누기
lcm = (n1 * n2) // gcd

print(gcd)
print(lcm)

#시간초과로 인하여 풀지 못함
'''
n1,n2 = 18,24
n1,n2 = map(int,input().split(' '))
if n1>n2:
    n1,n2 = n2,n1
tn1 = 0
tn2 = n1*n2

for i in range(n1,0,-1):
    if n1%i==0 and n2%i==0:
        tn1 =i
        break

for i in range(n1,n1*n2,tn1):
    if i%n1==0 and i%n2==0:
        tn2 = i
        break
print(tn1)
print(tn2)

최소공배수는 두수의 곱 나누기 최대공약수 로 구하기만해도 시간 초과는 나지 않음

다른 방법으로는 유클리드 호제법을 사용하는 것인데

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
b가 0이 아닐 때 까지 계속 나누는 방법
ex) gcd(18,24)
a,b = 24, 6
a,b = 6, 0 
return 6
이렇게 해서 최대 공약수를 구할 수 있다. 


'''
#한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
d = [0]*100

#피보나치 함수를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
#탑다운 방식 : 큰문제를 해결하기 위해 작은 문제를 호출하는 방법
def fibo(x):
    if x==1 or x==2:
        return 1
    
    if d[x]!=0:
        return d[x]

    d[x] = fibo(x-1)+fibo(x-2)
    return d[x]

def fibo2(x):
    if x==1 or x==2:
        return 1
    return fibo2(x-1)+fibo2(x-2)

db = [0]*100
db[1] = 1
db[2] = 1
n = 99
    
for i in range(3,n+1):
    db[i] = db[i-1]+db[i-2]

print(db[n])   

print(fibo(99))
# print(fibo(13))
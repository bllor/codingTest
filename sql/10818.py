n = int(input())

a = input().split(' ')

min = 0
max = 0
for i in range(n):
    if i ==0:
        min=int(a[i])
    
    if min > int(a[i]):
        min = int(a[i])
        
    if max < int(a[i]):
        max = int(a[i])

print(min,max)
'''
위의 문제 풀이가 틀렸던 이유는 음수일 때를 고려하지 않아서이다.
현재 max는 0으로 되어있는데 배열의 수들이 전부 음수일 경우, 
음수 내에서 가장 큰 수를 구분하는 것이 아닌 max의 초기값인 0으로 출력된다.
'''
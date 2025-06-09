n = int(input())
arr = [0 if i**0.5%1 else 1 for i in range(n+1)] # 제곱수는 1로 저장
print(arr)
min_ = 4
for i in range(int(n**0.5), 0, -1):
    if arr[n] : # n이 제곱수일 경우
        min_=1
        break
    elif arr[n-i**2] : # 나머지가 제곱수일 경우
        min_=2
        break
    else:
        for j in range(int((n-i**2)**0.5), 0, -1):
            if arr[(n-i**2)-j**2]: # 제곱수를 한번 더 뺀 나머지가 제곱수일 경우
                min_=3
print(min_)

'''
0부터 n까지 제곱인 값은 1로 그렇지 않은 수는 0으로 저장한다
모든 자연수는 자연수 4개 혹은 그 이하의 제곱근의 합으로 표현할 수 있으므로, 최대값인 4를 기본값으로 둔다
for i in range(int(n**0.5), 0, -1):
    if arr[n] : # n이 제곱수일 경우
        min_=1
        break
    n이 25일 경우 arr[25]는 1이므로 min은 1개가 된다
    elif arr[n-i**2] : # 나머지가 제곱수일 경우
        min_=2
        break
    n =29일 경우 arr[29-2**2]는 1이되는데
    29는 5^2+2^2와 같다.
    그래서 Min = 2가 된다.
    else:
        for j in range(int((n-i**2)**0.5), 0, -1):
            if arr[(n-i**2)-j**2]: # 제곱수를 한번 더 뺀 나머지가 제곱수일 경우
                min_=3
    n = 38일 때 5^2+2^2+3^2가 되는데
    for j in range(5,0,-1):
        for arr[(38-4)-9] -> arr[25]=1이 되므로 min = 3이 된다.
    여기에도 속하지 않을 경우 min = 4가 된다.
    
'''
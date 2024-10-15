# a부터 b까지의 합 구하기

a = int(input())
b= int(input())

if a>b:
    a,b = b,a

for a in range(a,b+1,1):
    print(a)

'''    
for a in range(a,b+1,1):
    print(a)
처럼 range안에 a,b를 넣어야 a~b를 1만큼 증가하며 출력한다.
여기에


for a in range(b+1)
이렇게 한다면 a의 값을 받지 못하고, a는 range를 나타내는 수로
0부터 시작한다.    
'''
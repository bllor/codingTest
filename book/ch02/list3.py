#enumerate() : 인덱스와 원소를 짝지어 튜플로 꺼내는 내장함수

x=['j','o','h','n']

# for i in range(len(x)):
#     print(f'{x[i]}')
    
# for i, name in enumerate(x,1): 
# x,n :n번부터 시작
#name은 x의 i번째 항목을 뜻한다.
#     print(f'{i},{name}')
    
for i, name in enumerate(x,2):
    print(f'{i},{name}')

# str= 'smupc'
str ='s'
# str = input()
for i in range(len(str)):
    num1 = f'{ord(str[i])}'
    num2 = 0
    print(list(map(int,num1)))
    
    # for j in range(len(num1)):
    #     num2+=int(num1[j])
    # print(str[i]*num2)
    
'''
아스키 코드를 합치는 과정에서 나는 for문을 한 번 더 사용했는데
map을 이용하면 조금 더 단순하게 코드를 작성할 수 있다.
num2 = sum(map(int,num1))를 하게 되면 num1을 하나씩 더한 값이 나온다.
list(map(int,num1))을 할경우 num1의 원소가 하나씩 출력되는 것을 확인할 수 있다.
'''
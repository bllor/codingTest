

def meCode(n):
    for i in range(n):
        for j in range(i+1):
            print(' '*(n-i-1)+'*'*(i+1))
    print()

def meCode2(n):
    for i in range(n):
        print(' '*(n-i-1)+'*'*(i+1))

 
def bookCode(n):
    for i in range(n):
        for _ in range(n-i-1): 
            print(' ',end='')
        for _ in range(i+1):
            print('*',end='')
        print()    
n=5
# meCode(n)
# meCode2(n)
bookCode(n)

'''
내가 처음 작성한 코드인
def meCode(n):
    for i in range(n):
        for j in range(i+1):
            print(' '*(n-i-1)+'*'*(i+1))
    print()
이것은
n이 3일 경우,
  *
 **
 **
***
***
***

이런 식으로 출력되었는데, 그 이유는
for j in range(i+1):
            print(' '*(n-i-1)+'*'*(i+1))
이 부분 때문이다.
여기서 *값이 i+1만큼 반복되기 때문에 2이상부터는 반복되어 출력이 된다.
그래서 책에서 요구한 사항과는 다르게 출력되었고,
그래서 meCode2로 변경하였다.

책이 작성한 코드와 내가 작성한 코드 중 어떤 것이 더 효율적인지 chatGPT에게 물어보니
내가 작성한 코드가 더 효율적이라고 하였다.
그 이유는 한 번의 출력으로 공백과 별을 출력하기 때문이라고 한다.
'''
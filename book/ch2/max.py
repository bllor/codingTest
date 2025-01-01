from typing import Any, Sequence #Any: 임의의 자료형, Sequence는 리스트. 바이트배열, 문자열형, 튜플형, 바이트열행을 뜻한다.

def max_of(a:Sequence)->Any: #건네받는 매개변수는 sequence형이고, 반환하는 값은 any로 한다는 뜻
    maximum = a[0]
    for i in range(len(a)):
        if maximum < a[i]:
            maximum = a[i]
    return maximum

'''
__name__은 모듈의 이름으로, 파일명을 뜻한다.
만약 파일명이 max2.py일 경우, __name__은 max2가 된다
스크립트 프로그램이 직접 실행될 때 변수 __name__은 __main__이 된다.
터미널에 python3 book/ch2/max.py처럼 직접 파일을 실행할 경우,
변수 __name__은 __main__이 된다는 뜻이다.

이름이 __main__일 경우에만 If절 밑부분을 사용한다는 뜻이고,
이렇게 사용하는 이유는 위의 함수는 max_of를 재사용하기 위해서이다.
만약 max2.py에서 max_of를 임포트 하여 사용하면 if __name__==='__main__' 아래 부분은 실행되지 않는다.

''' 
if __name__=='__main__':
    
    print('배열의 최대값 구하기')
    n = int(input('number'))
    x=[None]*n;
    for i in range(n):
        x[i]= int(input(f'x[{x[i]}]의 값'))
    print(f'최대값은 {max_of(x)}')
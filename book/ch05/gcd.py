#gcd(greatest common divisor) : 최대 공약수

def gcd(x:int, y:int)->int:
    if y==0:
        return x
    else:
        print(f'gcd x : {x}')
        print(f'gcd y : {y}')
        print('-----------')
        return gcd(y,x%y)

if __name__=='__main__':
    x=int(input('X'))
    y=int(input('Y'))
    gcd(x,y)
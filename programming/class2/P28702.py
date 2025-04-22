'''
1  2  f 4  b f 7  8  f b 11 f 13 14 fb 
16 17 f 19 b f 22 23 f b 26 f 28 29 fb 
31 32 f 34 b f 37 38 f b 41 f 43 44 fb 
'''
import sys
arr= [None]*3
for i in range(3):
    arr[i]= sys.stdin.readline()


# arr= ['Fizz','Buzz','9']
n = 0
ao = 0
for i in range(3):
    if arr[i][0] != 'F' and arr[i][0] !='B':
        # print(arr[i])
        ao = 3-i 
        n = int(arr[i])+ao
        # 숫자가 나온 문자열의 순서 다음 몇 번째 문자열이 출력되어야 하는지
        # i가 0일 경우, n보다 3만큼 더 큰 수가 출력되어야 함
        break
b = n%15  #몫
a = n//15 #나머지

if b == 0:
    print('FizzBuzz')
elif n%3 == 0:
    print('Fizz')
elif n%5 == 0:
    print('Buzz')
else:
    print(n)

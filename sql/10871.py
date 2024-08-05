n,m =map(int, input().split(' '))
a = input().split(' ')

ls = []
for i in range(n):
    if int(a[i])<m:
      print(a[i], end = " ")
'''
출력을 띄워쓰기로 구분하고 싶을 때는 print(num[i],end = " ")를 사용하면 된다.
'''
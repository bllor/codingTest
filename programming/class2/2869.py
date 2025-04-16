import math
a,b,v = map(int, input().split(' '))

n = ((v-a)/(a-b))+1 
print(math.ceil(n))
'''
v = a+(a-b)*n-1
v - a /a-b = n-1

v-a +1=n
a-b
'''     

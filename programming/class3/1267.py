import math
import sys
N = input()
arr = sys.stdin.readline().rstrip().split(' ')

y_price = 0
s_price = 0

for time in arr:
    y_price += math.ceil((int(time)+1)/30)*10
    s_price += math.ceil((int(time)+1)/60)*15
if y_price > s_price:
    print(f'M {s_price}')
elif s_price > y_price:
    print(f'Y {y_price}')
else:
    print(f'Y M {y_price}')
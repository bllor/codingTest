import math
# 소수점이 있을 경우 math.ceil을 사용하면 올림이 된다.
l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

day = math.ceil(a/c)

if a/c<b/d:
    day = math.ceil(b/d)
print(l-day)
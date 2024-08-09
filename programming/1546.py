n =int(input())

a = map(int, input().split(" "))

a = list(a)
mn = max(a)
avg = sum(a)/n
print(avg*100/mn)    
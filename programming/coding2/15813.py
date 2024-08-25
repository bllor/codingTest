n = int(input())


str = input()
# print(ord(str))
tn =0
for i in range(n):
    tn +=(ord(str[i])-64)
print(tn)
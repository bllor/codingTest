str = input()

a = 1
for i in range(len(str)//2):
    if str[i] == str[len(str)-1-i]:
        continue
    else:
        a = 0
        break
print(a)
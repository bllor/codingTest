n = int(input())
str = input()
tn = 0
for i in range(len(str)):
    n1 = ord(str[i])-96
    n2 = n1*31**i
    tn +=n2
print(tn%1234567891)

#A mod M은 A를 M으로 나누었을 때 나머지를 뜻한다. 
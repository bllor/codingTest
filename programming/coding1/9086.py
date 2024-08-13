n = int(input())

for i in range(n):
    str = input()
    if len(str)<2:
        print(str+str)
    else:
        print(str[0]+str[len(str)-1])
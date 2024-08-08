n = int(input())

for i in range(n):
    t, s = input().split(' ')
    
    for q in range(len(s)):
        for j in range(int(t)):
            print(s[q],end='')
    print('')
n,m = map(int, input().split(' '))

dic = [0 for i in range(n)]
for a in range(m):
    i,j,k = map(int, input().split(' '))
    for q in range(i-1,j):
        dic[q]=k
print(str(dic).replace('[','').replace(']','').replace(',',''))
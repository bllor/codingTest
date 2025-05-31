N = int(input())
arr=set()
for i in range(N):
    iq = input()
    if iq == 'empty':
        arr = set()
        continue
    elif iq =='all':
        continue
    op,n = iq.split(' ')
    if op =='add':
        arr.add(n)
    elif op =='remove':
        arr.discard(n)
    elif op =='check':
        print(list(arr).count(n))
    elif op=='toggle':
        if list(arr).count(n):
            arr.discard(n)
        else:
            arr.add(n)
        
            
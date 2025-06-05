
arr = ['1','11 2','111 21 12 3',None,None,None,None,None,None,None]
for i in range(4,11):
    N=i
    # print('N',N)
    n_arr = []
    for i in range(1,N):
        # print(i,N-i)
        n_arr.append(f'{i} {N-i}')

    s_arr = set()
    for n_str in n_arr:
        n1,n2 = map(int,n_str.split(' '))
        ns1 = arr[n1-1].split(' ')
        ns2 = arr[n2-1].split(' ')
        # print(len(ns1))
        for ss1 in ns1:
            for ss2 in ns2:
                # print(ss1+ss2)
                s_arr.add(ss1+ss2)
    if arr[N-1]==None:
        arr[N-1]=' '.join(list(s_arr))

TN = int(input())
i_arr=[None]*TN
for i in range(TN):
    value = int(input())
    an = len(arr[value-1].split(' '))
    i_arr[i]=f'{an}'
print('\n'.join(i_arr))
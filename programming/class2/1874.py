import sys
input = sys.stdin.readline
N = int(input())
arr = [i for i in range(1,N+1)]
cmd_arr = [
4,
3,
6,
8,
7,
5,
2,
1,    
]

s_arr = []
no = 0

while len(s_arr)<N:
    for i in range(N):
        if len(s_arr)>0 and s_arr[len(s_arr)-1] ==cmd_arr[no]:
            s=''
    
               



'''
4 123
4 1234
3 123
6 1256
8 1278
'''    


'''
12345678
1
12
123
1234
123 4
12 43
1256 43
123 436
127 436
1278 436
127 4368
12 43687
1 436872
0 4368721


1
0 1
2 1
0 12
345 12
34 125
'''
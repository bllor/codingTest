'''
기능을 구현하지 못했음
일단, 10*13이런식으로 주어질 때 8*8로 나누지 못하였고,
8*8로 나누어서 흰색과 검은색이 교차되는지 확인하려고 [x,y],[x,y+1],[x,y+2],[x+1,y+1]이 같을 경우 수정해야한다고 가정했는데
이 풀이는 잘못된 풀이였음

'''
N,M = 10,13
arr=[
'BBBBBBBBWBWBW',
'BBBBBBBBBWBWB',
'BBBBBBBBWBWBW',
'BBBBBBBBBWBWB',
'BBBBBBBBWBWBW',
'BBBBBBBBBWBWB',
'BBBBBBBBWBWBW',
'BBBBBBBBBWBWB',
'WWWWWWWWWWBWB',
'WWWWWWWWWWBWB',    
]
f_arr = []
h_no = 0
while h_no+8<=N:
    v_no = 0
    n_arr = arr
    f_no = 0
    while v_no+8<=M:
        for i in range(h_no,8+h_no):
            # print(i,end=' ')
            for j in range(v_no,8+v_no):
                if j+2>=M or i+1>=N:
                    break
                # try:                        
                if n_arr[i][j] == n_arr[i][j+1] == n_arr[i][j+2] == n_arr[i+1][j+1]:
                        print(f'fix i:{i},j:{j}')
                        print('b',n_arr[i][j])
                        # n_arr[i][j] = 'W' if n_arr[i][j] =='B' else 'W'
                        if n_arr[i][j] =='B':
                            n_arr[i][j] = 'W'
                        else:
                            n_arr[i][j]='B'
                        print('a',n_arr[i][j])
                        f_no+=1
                # except:
                #         print(f'error i:{i},j:{j}')
                        
                #         break
        #         print(j,end=' ')
        #     print(' ')
        # print('----------')
        v_no+=1
    print(' ')
    f_arr.append(f_no)
    h_no+=1
print(f_arr)
# #N 가로, M: 세로


# arr=[
# 'BBBBBBBBBB',
# 'BBWBWBWBWB',
# 'BWBWBWBWBB',
# 'BBWBWBWBWB',
# 'BWBWBWBWBB',
# 'BBWBWBWBWB',
# 'BWBWBWBWBB',
# 'BBWBWBWBWB',
# 'BWBWBWBWBB',
# 'BBBBBBBBBB',    
# ]
# N,M = 10,13
# h_no = 0
# v_no =0
# f_arr = []
# while h_no+8<=N and v_no+8<=M:
#     f_no = 0
#     print(f'h:{h_no}. v:{v_no}')
#     for i in range(h_no,8+h_no):
#         print(i,end=' ')
#         for j in range(v_no,8+v_no):
#             print(j,end=' ')
#         print('--------')
#         #     # print(arr[i][j],end=' ')
#         #     print(f'i:{i}, j:{j}')
#         #     try:
#         #         if j+2 >M or i+1>N:
#         #             break
#         #         if arr[i][j] == arr[i][j+1] == arr[i][j+2] == arr[i+1][j+1]:
#         #             print(f'fix i:{i},j:{j}')
#         #     except:
#         #         print(f'error i:{i},j:{j}')
#         # print('')
#     # print('')
#     h_no+=1
#     v_no+=1
        
    






# # arr=[
# # 'WBWBWBWB',
# # 'BWBWBWBW',
# # 'WBWBWBWB',
# # 'BWBBBWBW',
# # 'WBWBWBWB',
# # 'BWBWBWBW',
# # 'WBWBWWWB',
# # 'BWBWBWBW',
# # ]

# # f_no = 0
# # # N,M = 8,8
# # N,M = 50,30
# # for i in range(0,N,8):
# #     if i +8 > N:
# #         break
# #     print(i)
# #     for q in range(0,M,8):
# #         if q + 8 >M:
# #             break
# #         print(q)

# # for i in range(N):
# #     for j in range(M):
# #         if j+2 >M or i+1 >N:
# #             break
# #         if arr[i][j] == arr[i][j+1] == arr[i][j+2] == arr[i+1][j+1]:
# #             print(f'i:{i},j:{j}')        

# # for i in range(N-1):
# #     for j in range(M-1):
# #         # print(f'i:{i},j:{j}',arr[i][j])
# #         if arr[i][j] == arr[i][j+1] ==arr[i][j+2]:
# #             print(f'i:{i},j:{j}')
# #             f_no+=1
# # print(f_no)
    
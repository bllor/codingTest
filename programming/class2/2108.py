import math
import sys
input = sys.stdin.readline
# N  = 5

# arr=[1,3,8,-2,4,5,4,5,3,-2,-1,-1]
N = int(input())
arr = [0]*N
for i in range(N):
    arr[i] = int(input())
arr.sort()
s_arr = list(set(arr))
n_arr = [0]*len(s_arr)
m_arr = []
maxNo  = 0
for i in range(len(s_arr)):
    cn = arr.count(s_arr[i])
    n_arr[i]= cn
    if cn>maxNo:
        m_arr=[]
        m_arr.append(s_arr[i])
        maxNo=cn
    elif cn==maxNo:
        m_arr.append(s_arr[i])
    
        
print(math.floor(sum(arr)/len(arr)))#산술평균
print(arr[len(arr)//2])#중앙값
if len(m_arr)==1: # 중앙평균
    print(m_arr[0])
else:
   m_arr.sort()
   print(m_arr[1])
print(arr[len(arr)-1]-arr[0])#범위


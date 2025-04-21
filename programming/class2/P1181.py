
N = int(input())
arr = [input() for _ in range(N)]
arr = list(set(arr))  # 중복 제거

# 길이 기준 오름차순 → 길이 같으면 사전순
arr.sort(key=lambda x: (len(x), x))

for word in arr:
    print(word)

'''
arr.sort(key=lamda x: (len(x), x))
파이썬의 커스텀 정렬방식이다
key는 정렬기준을 정하고 싶을 때 사용한다.
lamda는 간단한 함수를 한 줄로 표현할 수 있게 해주는 문법이다
arr.sort(key=lambda x: (len(x), x))
정렬할 때 기준이 되는 값을 (len(x),x)로 반환한다.
문자열 길이 기준으로 먼저 정렬하고, 길이가 같다면 알파벳 순으로 정렬한다.

ex)
arr = ['ant', 'banana', 'apple', 'cat']
단어	    정렬 기준 튜플
'ant'	    (3, 'ant')
'banana'	(6, 'banana')
'apple'	    (5, 'apple')
'cat'	    (3, 'cat')
정렬기준 튜플로 리턴된다.
그 다음 길이 기준으로 정렬한다음, 알파벳순으로 정렬을 다시 한다.


lamda x: (len(x),x)는 
def my_key(x):
    return (len(x),x)와 같다.
    
'''



#시간 초과 오류가 나고, 길이로 위치를 변경할 때 사전순 검증을 하지 않으므로 오류가 난다.
# N = int(input())
# arr =[None]*N
# for i in range(N):
#     arr[i]=input()

# arr1 = list(set(arr))
# arr1.sort()
# # print(arr1)

# for i in range(len(arr1)):
#     for j in range(i+1,len(arr1)):
#         if len(arr1[i]) >len(arr1[j]):
#             arr1[i],arr1[j]=  arr1[j],arr1[i]

# # print(arr1[k] for k in range(len(arr1)))   

# for k in range(len(arr1)):
#     print(arr1[k])
        
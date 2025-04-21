arr = ['ant', 'banana', 'apple', 'codexs','coxeqs','antd', 'apples', 'cat']

# arr.sort()
# 문자열일 경우 기본 정렬은 사전순, 숫자일 경우 오름차순

# 길이순으로 정렬변경
# arr.sort(key=len)
# for word in arr:
#     print(word)

# #길이의 역순으로 정렬
# arr.sort(key = lambda x : -len(x))
# for word in arr:
#     print(word)

# #알파벳순으로 정렬, 같은 알파벳이면 길이가 짧은 것이 앞으로 오게 하는 코드
# # arr = ['ant', 'banana', 'apple','and', 'cat']
# arr.sort(key=lambda x: (x,len(x)))
# for word in arr:
#     print('1',word)

# #단어 길이의 역순으로 정렬, 길이가 같으면 사전순으로 정렬
# # arr = ['ant', 'banana', 'apple','codexs','antd','apples', 'cat']
# arr.sort(key=lambda x: (-len(x),x))
# for word in arr:
#     print('2',word)
    
# #단어 길이의 역순으로 정렬, 길이가 같으면 사전의 역순으로 정렬
# # arr = ['ant', 'banana', 'apple', 'codexs','coxeqs','antd', 'apples', 'cat']
# arr.sort(key=lambda x: (len(x),x),reverse=True)  # 길이 역순, 사전 역순
# for word in arr:
#     print('3',word)
# #reverse= True를 통해서 사전 역순으로 정렬

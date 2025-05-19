from collections import deque

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    docs = list(map(int, input().split()))
    queue = deque([(i, doc) for i, doc in enumerate(docs)])

    count = 0
    while queue:
        cur = queue.popleft() # 첫번째 항목꺼내기
        if any(cur[1] < q[1] for q in queue): #중요도 비교
            queue.append(cur) #중요도가 낮으면 제일 뒤로 보냄     
        else:
            count += 1
            if cur[0] == m: # 몆 번째로 인쇄되는지 궁금한 번호와 배열의 번호가 같으면 
                print(count)# 번호 출력
                break
'''
문제를 이해하는데 오랜 시간이 걸렸음

'''
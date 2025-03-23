from collections import deque

queue = deque()

queue.append(5)
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()

# 1, 2, 3 출력
#deque객체를 리스트로 변경하고자 한다면 list(deque)처럼 사용하면 된다.

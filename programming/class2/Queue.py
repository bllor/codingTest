from collections import deque

queue = deque()

queue.extend([4,5])
print(queue)
queue.extend([1,2,3])
print(queue)
queue.extendleft([8,7,9])
print(queue)
from collections import deque

queue = deque()

def enqueue(queue, val):
    queue.append(val)

def dequeue(queue):
    if queue:
        return queue.popleft()


def peek(queue):
    if queue:
        return queue[0]

def is_empty(queue):
    return not queue

print(is_empty(queue))   # True

enqueue(queue, 10)
enqueue(queue, 20)
enqueue(queue, 30)

print(peek(queue))       # 10
print(dequeue(queue))    # 10
print(peek(queue))       # 20
print(dequeue(queue))    # 20

enqueue(queue, 40)

print(dequeue(queue))    # 30
print(dequeue(queue))    # 40

print(is_empty(queue))   # True
print(dequeue(queue))    # None
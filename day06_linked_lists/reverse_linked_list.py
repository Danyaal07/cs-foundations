class Node:
    def __init__(self, pVal, pNext = None):
        self.val = pVal
        self.next = pNext

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.next = n2
n2.next = n3
n3.next = n4

prev = None
curr = n1

while curr is not None:
    next_node = curr.next
    curr.next = prev
    prev = curr
    curr = next_node

while prev is not None:
    print(prev.val)
    prev = prev.next
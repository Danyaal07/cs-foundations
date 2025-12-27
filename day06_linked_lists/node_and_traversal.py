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

current = n1

while current is not None:
    print(current.val)
    current = current.next
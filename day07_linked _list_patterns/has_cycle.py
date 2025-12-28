class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n2   # cycle starts at node 2

    
def is_cycle(head):
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False


print(is_cycle(n1))  # True
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# list1
a1 = Node(1)
a2 = Node(2)
a3 = Node(4)
a1.next = a2
a2.next = a3

# list2
b1 = Node(1)
b2 = Node(3)
b3 = Node(4)
b1.next = b2
b2.next = b3

def merge_two_lists(list1, list2):
    dummy = Node(0)
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    # Append any remaining nodes from either list
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    return dummy.next
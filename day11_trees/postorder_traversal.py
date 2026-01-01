class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

def postorder_traversal(root):
    result = []
    stack = []
    current = root
    last_visited = None
    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.left
        peek_node = stack[-1]
        if peek_node.right is not None and last_visited != peek_node.right:
            current = peek_node.right
        else:
            result.append(peek_node.val)
            last_visited = stack.pop()
    return result

# Perform postorder traversal
traversal_result = postorder_traversal(root)
print(traversal_result)  # Output: [3, 2, 1]
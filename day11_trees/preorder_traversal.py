class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

def preorder_traversal(root):
    if not root:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val) 
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result

# Perform preorder traversal
traversal_result = preorder_traversal(root)
print(traversal_result)  # Output: [1, 2, 3]
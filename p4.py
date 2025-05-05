class TreeNode:
    def _init_(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def are_symmetric(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif ((root1 is None) != (root2 is None)) or root1.val != root2.val:
        return False
    else:
        return are_symmetric(root1.left, root2.right) and are_symmetric(root1.right, root2.left)

def is_symmetric(root):
    if root is None:
        return True
    return are_symmetric(root.left, root.right)

tree = TreeNode(1)
tree.left = TreeNode(2, TreeNode(3), TreeNode(4))
tree.right = TreeNode(2, TreeNode(4), TreeNode(3))

print(is_symmetric(tree))  # Output: True

tree2 = TreeNode(1)
tree2.left = TreeNode(2, None, TreeNode(3))
tree2.right = TreeNode(2, None, TreeNode(3))

print(is_symmetric(tree2))
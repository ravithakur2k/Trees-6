# Time complexity is O(logn)
# Space is O(n)

# The logic is to use a stack and do an inorder traversal and add the BST check that if root val > low then only move towards left and similar for right, if root val < high only then
# explor right otherwise not needed

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = []
        result = 0
        while stack or root:
            while root:
                if root.val > low:
                    stack.append(root)
                    root = root.left
                else:
                    # No point exploring left subtree
                    stack.append(root)
                    break
            root = stack.pop()
            if root.val >= low and root.val <= high:
                result += root.val
            if root.val < high:
                root = root.right
            else:
                root = None
        return result
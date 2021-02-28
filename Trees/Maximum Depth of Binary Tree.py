# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # Approach1 : (40 ms, 16.1 MB)
        
        if root == None :
            return 0
        
        leftHeight = self.maxDepth(root.left) + 1
        rightHeight = self.maxDepth(root.right) + 1
        return max(leftHeight, rightHeight)
        
        # 한줄로 표현하면
        # return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
        
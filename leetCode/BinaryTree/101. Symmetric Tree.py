#101. Symmetric Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isSameTree(root.left, root.right)
    
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p==None and q==None:
            return True
        if p==None or q==None:
            return False
        if p.val!=q.val:
            return False

        return self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left)
        

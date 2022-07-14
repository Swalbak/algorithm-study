#94. Binary Tree Inorder Traversal

#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # if root==None:
        #     return []
        # return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)
    
        stack=[]
        result=[]
        cur=root
        while cur!=None or len(stack)!=0:
            while cur!=None:
                stack.append(cur)
                cur=cur.left
                
            cur=stack.pop()
            result.append(cur.val)
            if cur.right!=None:
                cur=cur.right
            else:
                cur=None
                
        return result
        

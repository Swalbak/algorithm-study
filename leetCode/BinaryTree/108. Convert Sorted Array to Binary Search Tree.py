#108. Convert Sorted Array to Binary Search Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums)==0:
            return
        
        pivot=len(nums)//2            
        root=TreeNode()
        root.val=nums[pivot]
        
        # if pivot==0:
        #     return root
        # elif pivot==len(nums):
        #     root.right=nums[0]
        #     return root
        
        root.right=self.sortedArrayToBST(nums[pivot+1:])
        root.left=self.sortedArrayToBST(nums[0:pivot])
        
        return root
                

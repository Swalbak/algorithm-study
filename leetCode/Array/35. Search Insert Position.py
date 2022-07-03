#35. Search Insert Position

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start=0
        end=len(nums)-1

        while start<end:
            mid=(start+end)//2
            if nums[start]<nums[

#1. Two Sum
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        #key: target-nums, value: index
        #target=nums[i]+nums[k] -> nums[i]=target-nums[k]
        sub_dict={}
        
        for i in range(len(nums)):
            #if nums[i] is equal to nums[k]
            if nums[i] in sub_dict:
                return [sub_dict[nums[i]], i]
            sub_dict[target-nums[i]]=i

target=7
nums=[3, 4, 6]
a=Solution()
print(a.twoSum(nums, target))

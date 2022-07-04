#35. Search Insert Position

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #using binary search
        start=0
        end=len(nums)-1
        mid=0
        while start<=end:
            mid=(start+end)//2
            if nums[mid]<target:
                start=mid+1
            elif nums[mid]>target:
                end=mid-1
            else:
                return mid
            
        #this conditional is already reflected in 'start' variable
        '''
        if nums[mid]<target:
            mid+=1
        return mid
        '''
        return start


nums=[1, 3, 5, 6]
target=5
a=Solution()
print(a.searchInsert(nums, target))
                

#27. Remove Element

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #Solution 1
        '''
        #using delete function
        index=0
        while index<len(nums):
            if nums[index]==val:
                del nums[index]
            else:
                index+=1
        '''

        #Solution 2
        '''
        #not using delete function
        index=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[index]=nums[i]
                index+=1
        return index
        '''

        #Solution 3(main Solution)

        #if nums list is empty
        if len(nums)==0:
            return 0

        #if val exists in nums list
        if val in nums:
            nums.sort()
            #find first index of val
            first_index=nums.index(val)
            #delete implements if it is equal to val
            while first_index<len(nums) and nums[first_index]==val:
                del nums[first_index]
            
        return len(nums)

nums=[0,1,2,2,3,0,4,2]
val=2
a=Solution()
print(a.removeElement(nums, val), nums)



    
            

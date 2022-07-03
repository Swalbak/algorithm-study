#26. Remove Duplicates from Sorted Array

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #Solution 1
        """

        #start index
        index=1

        #index's range: [0, len(nums)-1]
        while index<len(nums):
            #if duplicates exist, delete nums[index]
            #then index numbers are pulled forward one by one
            if nums[index-1]==nums[index]:
                del nums[index]
            else:
                index+=1
                
        return index
        """
    
        #Solution 2
        """
        #index to put the value(index+1)
        place_index=0
        #index of input value
        select_index=1
        
        while select_index<len(nums):
            #if duplicates exist, increase select_index(to find new value)
            #if a new value found, put it in the next index of place_index
            #(because we don't need duplicated value)
            if nums[place_index]!=nums[select_index]:
                place_index+=1
                nums[place_index]=nums[select_index]
                
            select_index+=1

        return place_index+1
        """

        #Solution 2-1 (main Solution)
        #replaced select_index to i(for)
        
        place_index=0
        for i in range(1, len(nums)):
            if nums[place_index]!=nums[i]:
                place_index+=1
                nums[place_index]=nums[i]

        return place_index+1
        

#실행부분
nums=[1, 1, 2]
a=Solution()
print(a.removeDuplicates(nums), nums)
            
            
        

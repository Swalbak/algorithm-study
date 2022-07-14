#496. Next Greater Element I

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1)==0:
            return
        
        stack=[]
        stack_result=[]
        ret_result=[]
        
        indices=list(map(lambda x:nums2.index(x), nums1))
        min_index=min(indices)
        start_index=len(nums2)-1
        
        for i in range(start_index, min_index-1, -1):
            result=-1
            while len(stack)!=0:
                if stack[-1]>nums2[i]:
                    result=stack[-1]
                    break
                stack.pop()
            stack.append(nums2[i])
            stack_result.append(result)
        
        for i in indices:
            ret_result.append(stack_result[len(nums2)-1-i])
            
        return ret_result

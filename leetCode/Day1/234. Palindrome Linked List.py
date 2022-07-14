# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        current=head
        #linked array to list
        int_array=[current.val]

        #make int_array
        while current.next!=None:
            current=current.next
            int_array.append(current.val)

        size=len(int_array)
        
        #if first integer is not equal to the last integer, return false
        #return int_array==int_array[::-1]
        for i in range(len(int_array)//2):
            if int_array[i]!=int_array[len(int_array)-1-i]:
                return False

        return True

        

#203. Remove Linked List Elements

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head==None:
            return
        
        if head.val==val:
            head=head.next
            head=self.removeElements(head, val)
        else:
            head.next=self.removeElements(head.next, val)
            
        return head

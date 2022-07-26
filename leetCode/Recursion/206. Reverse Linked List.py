#206. Reverse Linked List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseLinkedList(self, pre, head):
        if head==None:
            return pre
        node=head.next
        head.next=pre
        
        return self.reverseLinkedList(head, node)
        
        
        
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return
        
        return self.reverseLinkedList(None, head)
        
        

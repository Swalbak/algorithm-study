# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return
        
        cur=head
        pre=head.next
        
        while pre!=None:
            if cur.val!=pre.val:
                cur.next=pre
                cur=cur.next
            pre=pre.next
        cur.next=None
        return head

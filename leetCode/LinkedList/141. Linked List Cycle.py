#141. Linked List Cycle

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None:
            return False
        
        cur=head
        pre=head.next
        
        while pre!=None and pre.next!=None:
            if cur==pre:
                return True
            cur=cur.next
            pre=pre.next.next
        
        return False
    
#         if head==None:
#             return
#         array=[]
#         array.append(head)
#         cur=head
#         result=False
        
#         while cur.next!=None:
#             cur=cur.next
#             if cur in array:
#                 result=True
#                 break
#             array.append(cur)
#         return result
        

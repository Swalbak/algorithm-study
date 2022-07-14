# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        count=0
        
        cur_a=headA
        cur_b=headB

        while cur_a!=None and cur_b!=None:
            cur_a=cur_a.next
            cur_b=cur_b.next

        extra_node=cur_a
        extra_head=headA
        head=headB
        
        if cur_a==None:
            extra_node=cur_b
            extra_head=headB
            head=headA
            
        while extra_node!=None:
            extra_head=extra_head.next
            extra_node=extra_node.next

        while extra_head!=None:
            if extra_head is head:
                return head
            extra_head=extra_head.next
            head=head.next

        return
    
# class Solution(object):
#     def getIntersectionNode(self, headA, headB):
#         """
#         :type head1, head1: ListNode
#         :rtype: ListNode
#         """
#         count_a=0
#         count_b=0
        
#         cur_a=headA
#         cur_b=headB
        
#         while cur_a!=None:
#             count_a+=1
#             cur_a=cur_a.next
#         while cur_b!=None:
#             count_b+=1
#             cur_b=cur_b.next
            
#         min_list=headA
#         max_list=headB
#         if count_a>count_b:
#             min_list, max_list=max_list, min_list
        
#         for i in range(abs(count_a-count_b)): max_list=max_list.next
        
#         while max_list!=None:
#             if max_list is min_list:
#                 return max_list
#             max_list=max_list.next
#             min_list=min_list.next
        
#         return

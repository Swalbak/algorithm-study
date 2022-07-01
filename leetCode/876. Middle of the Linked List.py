#876. Middle of the Linked List

#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #mid node in linked list
        mid=head
        #pre node for jump two nodes
        pre=head

        #if pre.next is None, pre.next.next raise exception but doesn't execute 
        while pre.next!=None and pre.next.next!=None:
            pre=pre.next.next
            mid=mid.next
            
        #if size of list is even
        if pre.next!=None:
            mid=mid.next

    #    while pre.next!=None:
    #         if pre.next.next==None:
    #             mid=mid.next
    #             break
    #         pre=pre.next.next
    #         mid=mid.next
            
        return mid
        
    

#실행코드
array=[1, 2, 3, 4, 5]
head=ListNode()
head.val=array[0]
current=head

for i in array[1:]:
    node=ListNode()
    node.val=i
    current.next=node
    current=current.next
    
a=Solution()
print(a.middleNode(head))

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1==None:
            return list2
        elif list2==None:
            return list1

        head=list1
        cur=list1
        comp=list2
        
        if head.val>list2.val:
            head=cur=list2
            comp=list1

        while cur.next!=None:
            if cur.next.val>comp.val:
                cur.next, comp=comp, cur.next
            cur=cur.next
        
        cur.next=comp

        return head


list1=[1, 2, 4]
list2=[1, 3, 4]

head1=ListNode()
head1.val=list1[0]
cul1=head1

head2=ListNode()
head2.val=list2[0]
cul2=head2

for i in list1[1:]:
    new_node=ListNode()
    new_node.val=i
    cul1.next=new_node
    cul1=cul1.next

for i in list2[1:]:
    new_node=ListNode()
    new_node.val=i
    cul2.next=new_node
    cul2=cul2.next

a=Solution()
node=a.mergeTwoLists(head1, head2)

while node!=None:
    print(node.val, end=" ")
    node=node.next

        
            
        
        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p=head
        c=0
        while(p):
            p=p.next
            c+=1
        l=c//2
        k=0
        while(head):
            if(k==l):
                return head
            
            head=head.next
            k+=1
        

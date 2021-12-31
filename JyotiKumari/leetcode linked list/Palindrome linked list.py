 Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        slow = fast = head
        
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            
        prev = None
        while slow:
            temp = slow
            slow = slow.next
            temp.next = prev
            prev = temp
            
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
            
        return True
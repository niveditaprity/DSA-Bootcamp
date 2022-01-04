# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current = head
        arr = [current.val]
        
        while current.next:
            current = current.next 
            arr.append(current.val)
        
        if arr[::-1] == arr:
            return True
        return False

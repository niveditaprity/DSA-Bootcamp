# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        count = 0
        current = head
        
        while current != None:            
            current = current.next
            count += 1
            
        if count % 2 == 0:
            mid = count // 2
        else:
            mid = (count + 1) // 2
        
        first_half = []
        second_half = []
        current = head
        index = 0
        
        while current != None:
            if index < mid:    
                first_half.append(current)            
            else:
                second_half.append(current)
            current = current.next
            index += 1
        second_half = list(reversed(second_half))
        current = first_half.pop(0)
        for i in range(count - 1):            
            if i % 2 == 0:
                current.next = second_half.pop(0) 
            else:
                current.next = first_half.pop(0)  
            current = current.next
        current.next = None
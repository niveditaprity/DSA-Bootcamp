# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        # If both list are present, assign start to min first element of the two lists
        elif list1.val <= list2.val:
                temp=list1
                list1=list1.next
                
                
        else:
                temp=list2
                list2=list2.next
                
                
        #store address of temp to be returned in the end
        result=temp
        
        while (list1 and list2):
                # Compare elements of lists and add min to temp
                if (list1.val <= list2.val):
                    temp.next=list1
                    list1=list1.next
                    # print(temp.val, "List1", list1)
                    temp=temp.next
                else:
                    temp.next=list2
                    list2=list2.next
                    # print(temp.val, "List2", list2)
                    temp=temp.next
                    
                    
                # If list1 is longer than list2
        while list1:
            temp.next=list1
            list1=list1.next
            # print(temp.val, "List1", list1)
            temp=temp.next
                
            # If list2 is longer than list1
        while list2:
            temp.next=list2
            list2=list2.next
            # print(temp.val, "List2", list2)
            temp=temp.next
            
            # Return final result with both the lists appended in ascending order
        return(result)
        
        # Return blank list if both lists are empty
        return list1
                

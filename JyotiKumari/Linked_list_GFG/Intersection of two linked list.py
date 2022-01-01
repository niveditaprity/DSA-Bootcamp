class Solution:
    def findIntersection(self, head1, head2):
        # code here
        # return head of intersection list
        if(head1 is None or head2 is None):
            return None
        
        dup_val = dict()
        curr = head2
        
        while curr:
            dup_val[curr.data] = 1
            curr = curr.next
            
        curr = head1
        h3 = Node(0)
        prev = h3
        
        while curr:
            fwd = curr.next
            curr.next = None
            if curr.data in dup_val:
                prev.next = curr
                prev = curr
            curr = fwd
        head = h3.next
        h3.next = None
            
        return head
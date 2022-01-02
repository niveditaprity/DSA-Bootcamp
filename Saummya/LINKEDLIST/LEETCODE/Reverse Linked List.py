class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes=[]
        temp=head
        while temp:
            nodes.append(temp)
            temp=temp.next
            
        ans=None
        while nodes:
            node=nodes.pop()
            if not ans:
                ans=node
            node.next=nodes[-1] if nodes else None
            
        return ans

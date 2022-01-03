class Solution:
    def sortedInsert(self, head1,key):
        # code here
        # return head of edited linked list
        if head1 is None:
            head1 = Node(key)
        
        elif head1.data >= key:
            temp = head1
            head1 = Node(key)
            head1.next = temp
        
        else:
            currNode = head1
            while( currNode.next != None and currNode.next.data < key):
                currNode = currNode.next
                
            temp = Node(key)
            temp.next = currNode.next
            currNode.next = temp
        
        return head1

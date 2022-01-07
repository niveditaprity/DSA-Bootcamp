#Function to find intersection point in Y shaped Linked Lists.
def intersetPoint(head1,head2):
    #code here
    temp1=head1
    temp2=head2
    fakeNode=Node(0)
    while True:
        if head1.next!=fakeNode and head1.next!=None:
            head1=head1.next
            #point the previously traversed node to fakenode
            temp1.next=fakeNode
            temp1=head1
            
        elif head1.next==fakeNode:
            #Intersection point detected by linked list 1
            return head1.data
            
            #checking if next node is not fakenode or if it reached the end of linked list 1
        if head2.next!=fakeNode and head2.next!=None:
            head2=head2.next
            #point the previously traversed node to fakenode
            temp2.next=fakeNode
            temp2=head2
            
        elif head2.next==fakeNode:
            #Intersection point detected by linked list 1
            return head2.data  
            
        if head1.next==None and head2.next==None:
            if head1==head2:
                #Intersection point detected by linked list 1 and linked list 2 together,
                #i.e, if there are no nodes after intersection
                return head1.data
                
            return -1

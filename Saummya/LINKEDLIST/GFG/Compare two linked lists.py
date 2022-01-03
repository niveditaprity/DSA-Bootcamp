
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
def compare(head1, head2):
    #return 1/-1/0
    n1=head1
    n2=head2
    
    while n1 and n2:
        if n1.data!=n2.data:
            if n1.data>n2.data:
                return 1
            else:
                return -1
        else:
            n1=n1.next
            n2=n2.next
            
    if n1:
            return 1
    if n2:
            return -1
            
    return 0

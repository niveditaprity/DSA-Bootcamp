
'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

def multiplyTwoList(head1, head2):
    # Code here
    num1 = ""
    while head1.next:
        num1+=str(head1.data)
        head1 = head1.next
    num1 += str(head1.data)
    
    num2 = ""
    while head2.next:
        num2+=str(head2.data)
        head2 = head2.next
    num2 += str(head2.data)
    
    return (int(num1)*int(num2))%MOD

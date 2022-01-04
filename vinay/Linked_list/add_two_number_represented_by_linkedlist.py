
''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
def reverse(head):
    prev=None
    curr=head
    s=0
    while(curr):
        s+=1
        n=curr.next
        curr.next=prev
        prev=curr
        curr=n
    return [prev,s]
class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        # code here
        # return head of sum list
        h1=reverse(first)[0]
        n=reverse(first)[1]
        h2=reverse(second)[0]
        m=reverse(second)[1]
        h=LinkedList()
        carry=0
        if(n>m):
            while(m):
                if(carry==1):
                    d1=h1.data
                    d2=h2.data
                    p=d1+d2+1
                    carry=(d1+d2+1)//10
                    p=p%10
                    h.insert(p)
                    n-=1
                    m-=1
                    
                    
                    h1=h1.next
                    h2=h2.next
                else:
                    d1=h1.data
                    d2=h2.data
                    
                    carry=(d1+d2)//10
                    p=(d1+d2)%10
                    h1=h1.next
                    h2=h2.next
                    h.insert(p)
                    m-=1
                    n-=1
            while(n):
                d1=h1.data+carry
                carry=d1%10
                h.insert(d1)
                h1=h1.next
                n-=1
            if(carry):
                h.insert(1)
            
                
        else:
            while(h1 and h2):
                if(carry==1):
                    d1=h1.data
                    d2=h2.data
                    p=(d1+d2+1)%10
                    carry=(d1+d2+1)//10
                    h1=h1.next
                    h2=h2.next
                    h.insert(p)
                    m-=1
                    n-=1
                else:
                    d1=h1.data
                    d2=h2.data
                    p=(d1+d2)%10
                    carry=(d1+d2)//10
                    h.insert(p)
                    h1=h1.next
                    h2=h2.next
                    n-=1
                    m-=1
            while(h2):
                d2=h2.data+carry
                p=d2%10
                h2=h2.next
                h.insert(p)
                carry=d2//10
                m-=1
            while(h1):
                d2=h1.data+carry
                p=d2%10
                h.insert(p)
                carry=d2//10
                n-=1
                h1=h1.next
            if(carry):
                h.insert(carry)
        k=reverse(h.head)[0]
        return k
        
            
                
                
                    
            
                
            
                
                
            
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input().split() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input().split() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
        res = Solution().addTwoLists(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends

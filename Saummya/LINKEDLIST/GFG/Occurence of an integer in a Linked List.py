"""  
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
class Solution:
    def count(self, head, search_for):
        # Code here
        count=0
        head1=head
        while head1:
            while head1.data==search_for:
                count+=1
            head1=head1.next
            
        return count

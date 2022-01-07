class Solution:    
    def pairWiseSwap(self, head):
        if(head==None or head.next==None):
            return head;
        pre = None;
        cur = head;
        temp = None;
        while(cur!=None and cur.next!=None):
            temp = cur.next;
            cur.next = temp.next;
            temp.next = cur;
            if(pre==None):
                head=temp;
            else:
                pre.next=temp;
            pre = cur;
            cur = cur.next;
       
        return head;

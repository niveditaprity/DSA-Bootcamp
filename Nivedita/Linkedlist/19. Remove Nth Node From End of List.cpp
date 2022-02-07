class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (!head) return nullptr;

        ListNode*t1=head;
        
        ListNode*t2=head;
        
        for(int i=0;i<n;++i)
        {
            t1 = t1->next;
        }
        if(t1)
        {
           while(t1->next)
           {
               t1=t1->next;
               t2=t2->next;
           }
            ListNode*temp=t2->next;
            t2->next = t2->next->next;
            delete temp;
            
        }
        else
        {
          ListNode*temp=head;
            head=head->next;
            delete temp;  
        }
        return head;
    }
};

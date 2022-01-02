class Solution {
public:
    ListNode* reverseList(ListNode* head) {
     ListNode*Next,*prev=NULL;
        
      ListNode*curr=head;
        while(curr!=NULL)
        {
        Next=curr->next;
        curr->next=prev;
        prev=curr;
        curr=Next;
        }
        return prev;
        
        
    }
};

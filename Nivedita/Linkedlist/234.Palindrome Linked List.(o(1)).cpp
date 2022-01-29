/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
      //find middle node
        
        ListNode*slow=head;
        ListNode*fast=head;
        
        while(fast!=NULL&&fast->next!=NULL)
        {
            slow=slow->next;
            fast=fast->next->next; 
        }
        ListNode*prev=NULL;
        ListNode*curr=slow;
        ListNode*Next;
        while(curr!=NULL)
        {
            Next=curr->next;
            curr->next=prev;
            prev=curr;
            curr=Next;
        }
        ListNode*temp=head;
        while(prev!=NULL&&temp!=NULL)
        {
            if(prev->val!=temp->val)
            {
                return false;
            }
            temp=temp->next;
            prev=prev->next;
        }
        return true;
    }
};

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
     ListNode*fast=head;
    ListNode*slow=head;
        bool flag=0;
        while(fast!=NULL && fast->next!=NULL)
        {
            fast=fast->next->next;
            slow=slow->next;
            if(slow==fast)
            {
              flag=1;
                break;
            }
        }
        fast=head;
        
        if(flag==1)
        {
            while(fast!=slow)
            {
                slow=slow->next;
                fast=fast->next;
            }
            return slow;
        }
        return NULL;
    }
};

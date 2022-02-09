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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
      
        ListNode*p=head;
        
        for(int i=1;i<=n;i++)
        {
            p=p->next;
        }
        
        ListNode*q=head;
        
        if(p)
        {
            
            while(p->next)
            {
                p=p->next;
                q=q->next;
            }
            
            ListNode*temp=q->next;
            q->next=q->next->next;
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

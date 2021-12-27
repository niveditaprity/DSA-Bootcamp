class Solution {
public:
    ListNode* middleNode(ListNode* head) {
      ListNode*temp1=head;
        ListNode*temp2=head;
        while(temp1!=NULL&&temp1->next!=NULL)
        {
            temp2=temp2->next;
            temp1=temp1->next->next;
        }
        return temp2;
    }
};

class Solution
{
    public:
    //Function to check if the linked list has a loop.
    bool detectLoop(Node* head)
    {
       if(head==NULL)
       {
           return false;
       }
       Node*fast=head;
       Node*slow=head;
       while(fast!=NULL&&fast->next!=NULL)
       {
           fast=fast->next->next;
           slow=slow->next;
           if(slow==fast)
           {
               return true;
           }
       }
       return false;// your code here
    }
};

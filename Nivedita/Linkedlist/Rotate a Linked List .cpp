class Solution
{
    public:
    //Function to rotate a linked list.
    Node* rotate(Node* head, int k)
    {
      Node*temp=head;
      int n=k;
      while(temp->next!=NULL)
      {
          temp=temp->next;
      }
      temp->next=head;
      Node*ptr;
      while(k--)
      {
          ptr=head;
          head=head->next;
      }
      ptr->next=NULL;
      return head;// Your code here
    }
};

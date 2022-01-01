class Solution
{
    public:
    struct node *reverse (struct node *head, int k)
    { 
      struct node*prev=NULL;
      struct node*Next=NULL;
      struct node*curr=head;
      int count=0;
      while(curr!=NULL&&count<k)
      {
          Next=curr->next;
          curr->next=prev;
          prev=curr;
          curr=Next;
          count++;
          
      }
      if(Next!=NULL)
   {
       head->next=reverse(Next,k);
       
   }
   return prev;// Complete this method
    }
};

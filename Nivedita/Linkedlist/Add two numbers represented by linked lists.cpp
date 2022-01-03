class Solution
{
    public:
    struct Node* reverse(struct Node* head){
        struct Node *prev = NULL, *curr = head, *next = NULL;
        while(curr){
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }
    struct Node*add(struct Node*first,struct Node*second)
    {
        if(first==NULL)
    {
        return second;
    }
    if(second==NULL)
    {
        return first;
    }
    int sum=first->data+second->data;
    Node*p = new Node(sum%10);
    p->next=add(first->next,second->next);
    if(sum>=10)
    {
      p->next=add(p->next,new Node(1)); 
    }
    return p;
    }
    //Function to add two numbers represented by linked list.
    struct Node* addTwoLists(struct Node* first, struct Node* second)
    {
      struct Node*l1=reverse(first);
      struct Node*l2=reverse(second);
      return reverse(add(l1,l2));// code here
    }
};

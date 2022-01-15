/*The structure of the node is
struct Node
{
    int data;
    struct Node *next;
    
    Node(int x){
        data = x;
        next = NULL;
    }
    
};
*/
int fractional_node(struct Node *head, int k)
{
  Node* temp = head;
 
  int N=0;
  while(temp!=NULL)
  { 
  temp=temp->next;
  N++;
  }
  
   if(N%k!=0)
       N=N/k+1;
   else 
       N=N/k;
  
  while(--N)
  {
      head=head->next;
  }
  return head->data;
}

/*Node is defined as 
struct node
{
    int data;
    struct node* next;
    
    node(int x){
        data = x;
        next = NULL;
    }
}*head;
*/
class Solution
{
    public:
    int count(struct node* head, int search_for)
    {
      struct node*ptr = head;
      int count=0;
      while(ptr!=NULL)
      {
          if(ptr->data==search_for)
            count++;
        ptr=ptr->next;
      }
    return count;
    } 
};

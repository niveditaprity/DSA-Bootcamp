/*
  Print elements of a linked list on console 
  head pointer input could be NULL as well for empty list
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
     Node(int x){
         data = x;
         next  NULL;
     }
  }
*/
void display(struct Node *head)
{
   struct Node *ptr = NULL;
   ptr = head ;
   while(ptr != NULL)
   { printf("%d ",ptr->data);
     ptr=ptr->next;
       
   }
}

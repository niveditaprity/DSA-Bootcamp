//Function to insert a node at the begin of the linked list.
struct Node *insertAtBegining(struct Node *head, int x) {

  struct Node*temp=malloc(sizeof(struct Node));
  temp->data=x;
  temp->next=head;
  head=temp;
  
  return head;	
}


//Function to insert a node at the end of the linked list.
struct Node *insertAtEnd(struct Node *head, int x)  {
   
   struct Node *temp = (struct Node *) malloc(sizeof(struct Node));
   temp->data=x;
   temp->next=NULL;
   
   if (head == NULL) 
    {
    return temp;
    }
   
   else 
    {    
   struct Node* ptr=head;
   
   while(ptr->next!=NULL)
    {
       ptr=ptr->next;
    }
       ptr->next=temp;
       temp->next = NULL;
    }
   return head;
}

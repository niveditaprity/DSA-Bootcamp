//Function to insert a node in the middle of the linked list
struct Node* insertInMiddle(struct Node* head, int x)
{
   if(head==NULL)
     return NULL;
   struct Node *slow=head;
   struct Node *fast=head->next;
   struct Node*temp=malloc(sizeof(struct Node));
    temp->data = x;
    temp->next=NULL;
    
    
	 
	 while(fast!=NULL && fast->next!=NULL)
	 {
	     slow=slow->next;
	     fast=fast->next->next;
	 }
	 
	 temp->next=slow->next;
	 slow->next=temp;
	 
	 return head;
	 
}
    
    

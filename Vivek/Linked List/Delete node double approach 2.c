struct Node* deleteNode(struct Node *head_ref, int x)
    {   int count=1;
    struct Node* temp;
    struct Node* temp2;
    temp=head_ref;
    if(x==1)
    {
     temp2=temp->next;
     temp2->prev=NULL;
     temp->next=NULL;
     head_ref=temp2;   
    }
    else
    {
        while(count<x)
            {  temp=temp->next;
         count++;
              }
        /*temp2=temp->next; //node to be deleted
        temp->next=temp2->next;
        if(temp2->next!=NULL)
        {
             temp2->next->prev=temp;
        }
        temp2->prev=NULL;*/
        temp->prev->next=temp->next;
    }
      
      
return head_ref;
    }

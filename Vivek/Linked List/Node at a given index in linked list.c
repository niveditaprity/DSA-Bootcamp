
/* Print he nth node in the linked list Node is defined as 
/* Link list node
struct node
{
    int data;
    struct node* next;
    
    node(int x){
        data = x;
        next = NULL;
    }
}; 
*/

// Should return data of node at given index. The function may
//  assume that there are at least index+1 nodes in linked list
int GetNth(struct node* head, int index){
  
  
  node* temp = head;
  int counter = 1;
  while(counter<index){
      temp = temp->next;
      counter++;
  }
  return temp->data;
}
  

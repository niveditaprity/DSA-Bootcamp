
/* Linked list Node structure
struct Node
{
    char c;
    struct Node *next;
    
    Node(char x){
        c = x;
        next = NULL;
    }
    
};
*/

// Compare two strings represented as linked lists
int compare(Node *list1, Node *list2) 
{
    struct Node *ptr1=list1;
    struct Node *ptr2=list2;
     
     while(ptr1!=NULL && ptr2!=NULL )
     {
         if(ptr1->c > ptr2->c) 
           return 1;
         else if (ptr1->c < ptr2->c)
           return -1 ;
        
         ptr1=ptr1->next;
         ptr2=ptr2->next;
     }
     return 0;
}

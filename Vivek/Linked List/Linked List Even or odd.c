/*structure of a node of the linked list is as
struct Node
{
	int data;
	struct Node* next;
	
	Node(int x){
	    data = x;
	    next = NULL;
	}
	
};
*/
// Function should return 0 is length is even else return 1
int isLengthEvenOrOdd(struct Node* head)
{
  struct Node* ptr = head;
  int count=0;
  while(ptr!=NULL)
  { count++;
      ptr=ptr->next;
  }
  if(count%2 == 0)
    { return 0;
      return 1; }
}

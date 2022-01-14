
/*Structure of the node of the linled list is as

struct Node {
	int data;
	struct Node* next;
	
	Node(int x){
	    data = x;
	    next = NULL;
	}
};
*/
// your task is to complete this function 
// function should return sum of last n nodes
int sumOfLastN_Nodes(struct Node* head, int n)
{
      struct Node* temp=head;
      int sum=0,count=0;
      while(temp!=NULL)
      {   sum =sum+ temp->data;
          temp=temp->next;
          count++;
      }
      count = count-n;
      temp=head;
      while(count--)
      {
        sum = sum-(temp->data);
        temp=temp->next;
      }
      return sum;
}


/*Struture of the node of the linked list is as:

struct Node {
	int data;
	struct Node* next;
	
	Node(int x){
	    data = x;
	    next = NULL;
	}
	
};
*/
// Your task is to complete the function
// function should return the modular Node
// if no such node is present then return -1
int modularNode(Node* head, int k)
{
	int count=0,data=-1;
	
	while(head!=NULL)
	{   count++;
	    if(count%k==0)
	    {
	      data=head->data;  
	    }
	    head=head->next;
	}
	
	return data;
}

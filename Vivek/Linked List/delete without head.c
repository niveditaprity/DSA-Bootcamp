/*
struct Node {
  int data;
  struct Node *next;
  Node(int x) {
    data = x;
    next = NULL;
  }
}*head;
*/


class Solution
{
    public:
    //Function to delete a node without any reference to head pointer.
    void deleteNode(Node *del)
    {  Node *temp = del;
       Node *temp2 = temp->next;
       temp->data= temp2->data;
       temp->next=temp2->next;
       temp2->next=NULL;
       free(temp2);
       
    }

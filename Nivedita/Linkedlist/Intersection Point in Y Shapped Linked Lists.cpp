int count(Node*head)
{
    int count=0;
    while(head!=NULL)
    {
        count++;
        head=head->next;
    }
    return count;
}
int getintersection(int diff,Node*head1,Node*head2)
{
    Node*curr1=head1;
    Node*curr2=head2;
    
    for(int i=0;i<diff;i++)
    {
        if(curr1==NULL)
        {
            return -1;
        }
        curr1=curr1->next;
    }
    while(curr1!=NULL && curr2!=NULL)
    {
        if(curr1==curr2)
        {
            return curr1->data;
        }
        curr1=curr1->next;
        curr2=curr2->next;
    }
    return -1;
}
int intersectPoint(Node* head1, Node* head2)
{
  int d1=count(head1);
  int d2=count(head2);
  if(d1>d2)
  {
      int diff=d1-d2;
      return getintersection(diff,head1,head2);
  }
  else
  {
      int diff=d2-d1;
      return getintersection(diff,head2,head1);
  }
  return -1;
  // Your Code Here
}

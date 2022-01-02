  Node* merge(Node*head1,Node*head2)
{
 if(head1==NULL)
 {
  return head2;   
 }
 if(head2==NULL)
 {
     return head1;
 }
 Node*result;
 if(head1->data<head2->data)
 {
     result=head1;
     result->bottom=merge(head1->bottom,head2);
 }
 else
 {
     result=head2;
     result->bottom=merge(head1,head2->bottom);
 }
 return result;
}
Node *flatten(Node *root)
{
  if(root==NULL || root->next==NULL)
  {
      return root;
  }
  return merge(root,flatten(root->next)); // Your code here
}

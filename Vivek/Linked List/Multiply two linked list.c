
/* Linked list node structure
struct Node
{
    int data;
    Node* next;
    
    Node(int x){
        data = x;
        next = NULL;
    }
    
};*/

/*The method multiplies 
two  linked lists l1 and l2
and returns their product*/

/*You are required to complete this method*/
long long  multiplyTwoLists (Node* l1, Node* l2)
{
  long long MOD=1000000007;
long long r1=0,r2=0,result=0;
struct Node *p=NULL,*q=NULL;
p=l1,q=l2;
while(p!=NULL)
{
r1=(r1*10+p->data)%MOD;
p=p->next;
}
while(q!=NULL)
{
r2=(r2*10+q->data)%MOD;
q=q->next;
}
r1=r1%MOD;
r2=r2%MOD;
result=r1*r2;
return result%MOD;
}

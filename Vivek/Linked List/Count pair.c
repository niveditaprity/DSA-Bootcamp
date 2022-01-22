/* Structure of the node of the linked list is as
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
class Solution{
  public:
    // your task is to complete this function
    int countPairs(struct Node* head1, struct Node* head2, int x) {
       int count = 0;
    
    struct Node *p1, *p2;
    
    // traverse the 1st linked list
    for (p1 = head1; p1 != NULL; p1 = p1->next)

        // for each node of 1st list
        // traverse the 2nd list

        for (p2 = head2; p2 != NULL; p2 = p2->next)

            // if sum of pair is equal to 'x'
            // increment count
            if ((p1->data + p2->data) == x)
                count++;            
        
    // required count of pairs     
    return count;
    }
};

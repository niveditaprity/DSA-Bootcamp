#include <unordered_map>
class Solution
{
    public:
    //Function to remove a loop in the linked list.
    void removeLoop(Node* head)
    {
      
      unordered_map<Node*,int>mp;
      Node*temp=head;
      while(temp!=NULL)
      {
          if(mp[temp->next]>1)
          {
              temp->next=NULL;
          }
          mp[temp]++;
          temp=temp->next;
          
      }
      
      // code here
        // just remove the loop without losing any nodes
    }
};

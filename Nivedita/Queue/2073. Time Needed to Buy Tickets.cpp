class Solution {
public:
    int timeRequiredToBuy(vector<int>& tickets, int k) {
        
      int total=0;
        for(int i=0;i<tickets.size();i++)
        {
         if(tickets[i]>=tickets[k]&&i<=k)
         {
             total+=tickets[k];
             
         }
        else if(tickets[i]>=tickets[k]&&i>k)
        {
            total+=tickets[k]-1;
        }
            else
            {
                total+=tickets[i];
            }
        }
        return total;
    }
};

class Solution {
public:
    int countGoodSubstrings(string arr) {
        
      int count=0;
    map<char,int>mp;
        int j=3;
        int k=0,i=0;
        mp[arr[0]]++;
        mp[arr[1]]++;
        mp[arr[2]]++;
        if(mp[arr[0]]==1&&mp[arr[1]]==1&&mp[arr[2]]==1)
        {
            count++;
        }
        while(j<arr.size())
        {
    
            mp[arr[j]]++;
            mp[arr[k]]--;
            if(mp[arr[j]]==1&&mp[arr[j-1]]==1&&mp[arr[j-2]]==1)
               {
                   count++;
               }
               j++;
               k++;
        }
    
      return count;  
    }
};

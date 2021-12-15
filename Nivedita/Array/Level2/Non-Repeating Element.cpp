class Solution{
    public:
    int firstNonRepeating(int arr[], int n) 
    { 
      map<int,pair<int,int>>mp;
       int j=INT_MAX;
       for(int i=0;i<n;i++)
       {
           mp[arr[i]]={i+1,mp[arr[i]].second+=1};
           
       }
       for(int i=0;i<n;i++)
       {
        if (mp[arr[i]].second==1)
        {
            return arr[i];
        }
           
       }
       return 0;
         // Complete the function
        
    } 
  
};

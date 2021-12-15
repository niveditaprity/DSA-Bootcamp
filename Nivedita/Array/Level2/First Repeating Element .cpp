class Solution {
  public:
    // Function to return the position of the first repeating element.
    int firstRepeated(int arr[], int n) {
       map<int,pair<int,bool>>mp;
       int j=INT_MAX;
       for(int i=0;i<n;i++)
       {
           if(mp[arr[i]].second==true)
           {
              j=min(j,mp[arr[i]].first); 
           }
           mp[arr[i]]={i+1,true};
           
       }
       if(j<n)
       {
       return j;
       }
       return -1;// code here
    }
};

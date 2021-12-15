class Solution{   
public:
    int getPairsCount(int arr[], int n, int k) {
       map<int,int>mp;
       for(int i=0;i<n;i++)
       {
         mp[arr[i]]++;
       }
       int count=0;
      for(int i=0;i<n;i++)
      {
          count+=mp[k-arr[i]];
          if(k-arr[i]==arr[i])
          {
              count--;
          }
      }
      return count/2;
      // code here
    }
};

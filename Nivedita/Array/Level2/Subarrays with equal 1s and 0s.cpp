class Solution{
  public:
    //Function to count subarrays with 1s and 0s.
    long long int countSubarrWithEqualZeroAndOne(int arr[], int n)
    {
        map<int,int>mp;
        int sum=0;
        long long int count=0;
      for(int i=0;i<n;i++)
      {
          mp[sum]++;
          if(arr[i]==1)
          {
              sum++;
          }
          else
          {
              sum--;
          }
          count+=mp[sum];
          
      }
      return count;//Your code here
    }
};

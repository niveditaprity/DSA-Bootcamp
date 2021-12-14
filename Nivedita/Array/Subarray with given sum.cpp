class Solution
{
    public:
    //Function to find a continuous sub-array which adds up to a given number.
    vector<int> subarraySum(int arr[], int n, long long s)
    {
       vector<int>vec;
      int sum=0,m=0,l;
      for(int i=0;i<n;i++)
      {
          sum=sum+arr[i];
          if(sum==s)
          {
              l=i+1;
              m++;
              vec.push_back(m);
            vec.push_back(l);
            return vec;
          }
          while(sum>s)
          {
           sum=sum-arr[m];
           f++;
           if(sum==s)
           {
               l=i+1;
               m++;
                vec.push_back(m);
            vec.push_back(l);
            return vec;
           }
    }
      }
      return {-1};
    }
};

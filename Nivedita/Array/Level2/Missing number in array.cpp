class Solution{
  public:
    int MissingNumber(vector<int>& array, int n) {
      int t=array[0];
      for(int i=1;i<array.size();i++)
      {
          t^=array[i];
      }
      for(int i=1;i<=n;i++)
      {
          t^=i;
      }
      return t;// Your code goes here
    }
};

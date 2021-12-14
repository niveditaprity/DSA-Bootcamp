class Solution{
    public:
    void segregateElements(int arr[],int n)
    {
     vector<int>p,q;
     for(int i=0;i<n;i++)
     {
         if(arr[i]>0)
         {
             p.push_back(arr[i]);
         }
         else
         {
             q.push_back(arr[i]);
         }
     }
         for(int i=0;i<p.size();i++)
         {
             arr[i]=p[i];
         }
         for(int i=p.size();i<p.size()+q.size();i++)
         {
             arr[i]=q[i-p.size()];
         }
     }// Your code goes here
};

class Solution
{
    public:
    void sort012(int a[], int n)
    {
       int l=0,m=0,h=n-1;
       for(int i=0;i<n;i++)
       {
           if(a[m]==0)
           {
               int temp=a[m];
               a[m]=a[l];
               a[l]=temp;
               l++;
               m++;
           }
           else if(a[m]==2)
           {
               int t=a[m];
               a[m]=a[h];
               a[h]=t;
               h--;
           }
           else
           {
               m++;
           }
       }// coode here 
    }
    
};

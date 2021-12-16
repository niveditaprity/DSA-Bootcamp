class Solution{
public:

	void rearrange(int arr[], int n) {
	  int p[n],q[n];
	  int j=0,k=0;
	  for(int i=0;i<n;i++)
	  {
	    if(arr[i]<0)
	    {
	        q[k]=arr[i];
	        k++;
	    }
	    else
	    {
	        p[j]=arr[i];
	        j+=1;
	    }
	  }
	  int i=0,c=0,d=0;
	  while(i<n)
	  {
	      if(c<j)
	      {
	      arr[i++]=p[c++];
	      }
	      if(d<k)
	      {
	      arr[i++]=q[d++];
	      }
	  }// code here
	}
};

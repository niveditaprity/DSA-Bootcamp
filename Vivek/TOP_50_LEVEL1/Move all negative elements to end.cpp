// Question Link : https://practice.geeksforgeeks.org/problems/move-all-negative-elements-to-end1813/1
// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution{
    public:
    void segregateElements(int arr[],int n)
    {
 vector<int>p  ; 
 vector<int>q ;
 vector<int>ans;  
 int k=0 ; 
       for(int i =0 ; i <n ; i++) {
           if(arr[i]>0) p.push_back(arr[i]) ; 
           else q.push_back(arr[i]) ; 
       }
       for(auto  i  : p ) arr[k++]= i; 
       for(auto i : q)  arr[k++]=i ;    }
};

// { Driver Code Starts.
int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
		int n;
		cin>>n;
		int a[n];
		for(int i=0;i<n;i++)
		cin>>a[i];
		Solution ob;
		ob.segregateElements(a,n);
		
        for(int i=0;i<n;i++)
        cout<<a[i]<<" ";
		cout<<endl;
	}
}
  // } Driver Code Ends

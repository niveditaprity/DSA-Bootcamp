class Solution
{
    public:    
       vector <int> commonElements (int A[], int B[], int C[], int n1, int n2, int n3)
        {
           map<int,int>mp;
           vector<int>v;
           mp[A[0]]++;
           for(int i=1;i<n1;i++)
           {
               if(A[i-1]!=A[i])
               {
               mp[A[i]]++;
               }
           }
           mp[B[0]]++;
           for(int i=1;i<n2;i++)
           {
               if(B[i-1]!=B[i])
               {
               mp[B[i]]++;
               }
           }
            mp[C[0]]++;
           for(int i=1;i<n3;i++)
           {
               if(C[i-1]!=C[i])
               {
               mp[C[i]]++;
               }
           }
           for(auto x:mp)
           {
               if(x.second==3)
               {
                v.push_back(x.first);   
               }
           }
           if(v.size()==0)
           {
               v.push_back(-1);
           }
           return v;//code here.
        }

};

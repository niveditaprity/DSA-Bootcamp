class Solution
{
    public:
    //Function to find a continuous sub-array which adds up to a given number.
    vector<int> subarraySum(int arr[], int n, long long s)
    {
        // Your code here
        long long sum=0;
        vector<int>v;
        int j=0;
        for(int i=0; i<n; i++){
            sum = sum+arr[i];
            if(sum==s){
                v.push_back(j+1);
                v.push_back(i+1);
                return v;
            }
            else if(sum>s){
                while(sum>s){
                    sum = sum-arr[j];
                    j = j+1;
                }
                if(sum==s){
                    v.push_back(j+1);
                    v.push_back(i+1);
                    return v;
                }
            }
            
        }
        v.push_back(-1);
        return v;
    }
};
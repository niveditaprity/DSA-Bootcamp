class Solution {
public:
    int largestRectangleArea(vector<int>& arr)
    {
        int n=arr.size();
        if(n==0)
    return 0;
    
    stack<pair<int,int>> s; 
    vector<long long>left;
    
    for(int i=0;i<n;i++)
    {
        while(!s.empty() && s.top().first>=arr[i])
        {
            s.pop();
        }
        
        if(s.empty())
        {
            left.push_back(-1);
        }
        else
        {
            left.push_back(s.top().second);
        }
        s.push(make_pair(arr[i],i));
    }
    
    while(!s.empty())
    {
        s.pop();
    }
    
    
    vector<long long>right;
    for(int i=n-1;i>=0;i--)
    {
        while(!s.empty() && s.top().first>=arr[i])
        {
            s.pop();
        }
        
        if(s.empty())
        {
            right.push_back(n);
        }
        else
        {
            right.push_back(s.top().second);
        }
        s.push(make_pair(arr[i],i));
    }
    long long area=0;
    long long max_area=0;
    for(long long i=0;i<n;i++)
    {
        area=arr[i]*(right[n-1-i]-left[i]-1);
        max_area=max(area,max_area);
    }
    return max_area;
    
}




};

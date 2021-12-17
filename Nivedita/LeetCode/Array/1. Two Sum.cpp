class Solution {
public:
    vector<int> twoSum(vector<int>&nums, int target) {
        int n=nums.size();
        map<int,int>m;
        vector<int>ans;
        for(int i=0;i<n;i++)
        {
            m[nums[i]]=i;
        }
        for(int i=0;i<n;i++)
        {
            if(m[target-nums[i]]&& m[target-nums[i]]!=i)
            {
                ans.push_back(i);
                ans.push_back(m[target-nums[i]]);
                return ans;
            }
        }
        return {-1};
        
    }
};

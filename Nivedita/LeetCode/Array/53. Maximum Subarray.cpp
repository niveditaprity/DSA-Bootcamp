class Solution {
public:
    int maxSubArray(vector<int>& nums) {
      int maxr=INT_MIN;
        int maxs=0;
        for(int i=0;i<nums.size();i++)
        {
            maxs+=nums[i];
            if(nums[i]>maxs)
            {
                maxs=nums[i];
            }
            if(maxs>maxr)
            {
                maxr=maxs;
            }
        }
        return maxr;
    }
};

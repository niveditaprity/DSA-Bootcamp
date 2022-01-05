def maxSubArray(self, nums: List[int]) -> int:
       
        max1=nums[0]
        sum=0
        for n in nums:
            if sum<0:
                sum=0
            sum+=n
            max1=max(max1,sum)
        return max1

class Solution:
    def check(self, mid, nums, m):
        s=0
        count=0
        for i in range(len(nums)):
            if nums[i] > mid:
                return False
            s+=nums[i]
            if s>mid:
                count+=1
                s=nums[i]
        count+=1
        if count<=m:
            return True
		
        return False
        
    def splitArray(self, nums: List[int], m: int) -> int:
        start=0
        end=0
        answer=0
        for i in range(len(nums)):
            start=max(start,nums[i])
            end+=nums[i]
        while(start<=end):
            mid=(start+end)//2
            if(self.check(mid,nums,m)):
                answer=mid
                end=mid-1
            else:
                start=mid+1
			
        return answer
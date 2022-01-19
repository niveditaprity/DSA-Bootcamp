class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        nums=nums+nums
        s=[]
        res=[]
        n=len(nums)
        for i in range(len(nums)-1,-1,-1):
            if not s:
                res.append(-1)
            elif s and s[-1]>nums[i]:
                res.append(s[-1])
            elif s and s[-1]<=nums[i]:
                while s and s[-1]<=nums[i]:
                    s.pop()
                if not s:
                    res.append(-1)
                else:
                    res.append(s[-1])
            s.append(nums[i])
        res=res[::-1]
        return res[:n//2]

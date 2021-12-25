class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        l = []
        nums.sort()
        for i in range(len(nums)-3):
            if(i==0 or (nums[i]!=nums[i-1])):
                for j in range(i+1, len(nums)-2):
                    if(j==i+1 or (nums[j]!=nums[j-1])):
                        start = j+1
                        end = len(nums)-1
                        s = target-nums[i]-nums[j]
                        while(start<end):
                            if(nums[start]+nums[end]==s):
                                t = [nums[i], nums[j], nums[start], nums[end]]
                                l.append(t)
                                while(start<end and nums[start]==nums[start+1]):
                                    start+=1
                                while(start<end and nums[end]==nums[end-1]):
                                    end-=1
                                start+=1
                                end-=1
                            elif(nums[start]+nums[end]<s):
                                start+=1
                            else:
                                end-=1
        return l
                   
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = []
        nums.sort()
        for i in range(len(nums)-2):
            if(i==0 or (i>0 and nums[i]!=nums[i-1])):
                s = 0-nums[i]
                start = i+1
                end = len(nums)-1
                while(start<end):
                    if(nums[start]+nums[end]==s):
                        temp = [nums[i], nums[start], nums[end]]
                        l.append(temp)
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
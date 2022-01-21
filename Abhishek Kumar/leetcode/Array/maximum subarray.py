        maxi = nums[0]
        res = maxi
        n = len(nums)
        for i in range(1,n):
            maxi = max(maxi+nums[i],nums[i])
            if maxi > res:
                res = maxi
        return res

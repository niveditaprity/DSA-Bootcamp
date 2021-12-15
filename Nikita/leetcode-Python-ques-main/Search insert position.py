class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
       l = 0
       r = len(nums)

       while l < r:
          mid = (l + r) // 2

          if nums[mid] == target:
              return mid

          if nums[mid] < target:
             l = mid + 1

          if nums[mid] > target:
             high = mid - 1
       return l

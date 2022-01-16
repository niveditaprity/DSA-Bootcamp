class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        curr_max_sum = [0]
        for x in nums:
            curr_max_sum.append(curr_max_sum[-1] + x)

        ans = n+1
        hold = collections.deque()
        for y, Py in enumerate(curr_max_sum):
            while hold and Py <= curr_max_sum[hold[-1]]:
                hold.pop()

            while hold and Py - curr_max_sum[hold[0]] >= k:
                ans = min(ans, y-hold.popleft())

            hold.append(y)

        return ans if ans<n+1 else -1
            
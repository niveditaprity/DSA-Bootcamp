class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for i in range(1,3000):
            if i not in arr:
                k-=1
                if k==0:
                    return i

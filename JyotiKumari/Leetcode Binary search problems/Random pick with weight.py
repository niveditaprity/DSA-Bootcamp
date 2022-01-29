import random
import bisect

class Solution:

    def __init__(self, w: List[int]):
        self.weight = list(w)
        for i in range(1, len(w)):
            self.weight[i] += self.weight[i-1]

    def pickIndex(self) -> int:
        temp = random.randint(0, self.weight[-1]-1)
        return bisect.bisect_right(self.weight, temp)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
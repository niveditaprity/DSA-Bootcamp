# 1. BRUTE FORCE

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        for i in range(n):
            for j in range(i+1,n):
                if numbers[i]+numbers[j]==target:
                    return i+1,j+1
        
        
# 2. USING 2 POINTERS
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        sum1=0
        while(i!=j):
            sum1=numbers[i]+numbers[j]
            if sum1>target:
                j-=1
            elif sum1<target:
                i+=1
            else:
                return i+1,j+1

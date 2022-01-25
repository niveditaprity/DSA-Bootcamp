class Solution:
    def arrangeCoins(self, n: int) -> int:
        start=0
        end=n
        while start<=end:
            mid=(start+end)//2
            curr=mid*(mid+1)//2
            if curr==n:
                return mid
            elif n<curr:
                end=mid-1
            else:
                start=mid+1
        return end
 

'''
This question is easy in a sense that one could run an exhaustive iteration to obtain the result. That could work, except that it would run out of time when the input becomes too large. So let us take a step back to look at the problem, before rushing to the implementation.

Assume that the answer is kk, i.e. we've managed to complete kk rows of coins. These completed rows contain in total 1 + 2 + ... + k =k*(k+1)/2 coins
Instead of naive iteration, one could resort to another more efficient algorithm called binary search.
Time complexity : \mathcal{O}(\log N)O(logN).

Space complexity : \mathcal{O}(1)O(1).
'''

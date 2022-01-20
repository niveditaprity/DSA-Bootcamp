class Solution:
    def smallestpositive(self, array, n): 
        # Your code goes here  
        array.sort()
        res = 1
        for i in range (0, n ):
            if array[i] <= res:
                res = res + array[i]
            else:
                break
        return res
class Solution:
    def isLucky(self, n,counter=2):
        if counter > n:
            return True
        if n % counter == 0:
            return False
        
        next_pos = n-(n//counter)
        
        
        return self.isLucky(next_pos,counter+1)

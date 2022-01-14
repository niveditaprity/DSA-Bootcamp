class Solution:
    #Function to check if a string can be obtained by rotating
    #another string by exactly 2 places.
    def isRotated(self,str1,str2):
        N = len(str1)
        if str1[2:] + str1[:2] == str2:
            return True
        elif str1[N-2:] + str1[:N-2] == str2:
            return True
        return False

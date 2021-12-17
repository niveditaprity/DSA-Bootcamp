
#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code here
       
       
       for i in range(n):
            curr_sum = arr[i]
     
        
            j = i + 1
            while j <= n:
         
                if curr_sum == s:
                    #print ("Sum found between")
                    #print("indexes % d and % d"%( i, j-1))
                 
                    return i+1,j
                 
                if curr_sum > s or j == n:
                    break
             
                curr_sum = curr_sum + arr[j]
                j += 1
                
       return 0
               
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends

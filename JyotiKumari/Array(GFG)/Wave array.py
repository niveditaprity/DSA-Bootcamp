class Solution:
    #Complete this function
    #Function to sort the array into a wave-like array.
    def convertToWave(self,arr,N):
        #Your code here
        arr.sort
        for i in range(1,N):
            if(i%2!=0):
                temp = arr[i-1]
                arr[i-1] = arr[i]
                arr[i] = temp
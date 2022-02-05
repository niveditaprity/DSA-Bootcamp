    def minAdjDiff(self,arr, N):
  
        diff = abs(arr[1] - arr[0])
        
        for i in range(1,N):
            curr_diff = abs(arr[(i+1)%N] - arr[i])
            if curr_diff < diff:
                diff = curr_diff
        return diff

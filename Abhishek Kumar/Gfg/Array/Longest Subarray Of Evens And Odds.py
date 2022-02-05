    def maxEvenOdd(self,arr,n):
        max_count = 1
        curr_count = 1
        for i in range(1,n):
            if (arr[i-1] % 2 == 0 and arr[i] % 2 != 0) or (arr[i-1] %2 != 0 and arr[i] %2 == 0):
                curr_count += 1
            else:
                curr_count = 1
            if curr_count > max_count:
                max_count = curr_count
        return max_count

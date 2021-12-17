def findLongestConseqSubseq(self,arr, N):
        #code here
        longest_sequence = 0
        s = set()
        for i in range(N):
            s.add(arr[i])
        for i in range(N):
            element = arr[i]
            if((element-1) not in s):
                current_num = element
                current_sequence = 1
                while(element+1 in s):
                    element = element+1
                    current_sequence+=1
                longest_sequence = max(longest_sequence, current_sequence)
        return longest_sequence

#APPROACH-1------------ ISSUE-Time limit exceeded-----------
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        lst = []
        
        for i, j in itertools.combinations(range(len(nums) + 1), 2):
            lst.append(nums[i:j])
        
        res = []
        for i in sorted(lst):
            if sum(i) >=k:
                res.append(i)
              
        res.sort(key = lambda x:len(x))
        if res:
            return (len(res[0]))
        else:
            return -1
        
        
        
   #APPROACH-2--------------
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        queue = deque()
        curr = 0
        minCount = 0
        out = -1
        for num in nums:
            # if queue is empty, append num if positive
           
            if len(queue) == 0:
                if num > 0:
                    queue.append((num, 1))
                    curr = num
                    minCount = 1
                    # if one number is already enough, just return 1
                    # small optimization, not a big deal
                    if curr >= k:
                        return 1
                    
            else:
            # if queue is not empty
            
                # if num is positive, increment current array sum and counter
                if num > 0:
                    queue.append((num, 1))
                    curr += num
                    minCount += 1

                # if num is not positive, we need to determine 
                # whether it is meaningful to append,
                # or just empty the queue and start fresh
                else:
                    # if current sum adding the number is still positive,
                    # it will be meaningful to proceed, consider case:
                    # [1,1,1,1,5,-1,5], k = 9
                    if curr + num > 0:
                        curr += num
                        temp = 1
                        # merge the value and count to the elements in queue
                        # [(10,1), (20,1), (-25,1)] -> [(5,3)]
                        while queue:
                            val, count = queue.pop()
                            if val + num > 0:
                                queue.append((val+num, count + temp))
                                break
                            else:
                                num += val
                                temp += count
                        
                        minCount += 1
                    # if current sum adding the number is not positive,
                    # then it's meaningless to continue with present queue,
                    # just start fresh, consider case
                    # [1,-2,3], k = 3
                    else:
                        curr = 0
                        queue = deque()
            # after processing the number, we recursively popleft
            # till current sum is smaller than k, update output when necessary
            while curr >= k:
                if out == -1 or out > minCount:
                    out = minCount
                val, count = queue.popleft()
                curr -= val
                minCount -= count

        return out
    

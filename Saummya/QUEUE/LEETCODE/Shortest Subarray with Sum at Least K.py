
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
    
    '''
    Explanation:
    The idea behind this problem is a variation of sliding window. What makes this problem tricky is the presense of non positive numbers in the array. We need to have some more delicated logic on how we want to pop the left element of the queue.

My implementation is to let the queue be a 2-tuple data structure: each element of the queue is like (value, count) format. I will further explain what each of them represent. Through each iteration, we keep track of two variables: current_sum and current_count

We start with an empty queue, iterate through the number list. For each number, we have two cases, positive or non-positive, to consider.
Positive case is straightforward: we just append the 2-tuple (num, 1) to our queue. "1" means this "num" is consist of the sum of one element.
Non-positive case requires some more logic:

When the queue is empty, it's meaningless to include this number into our subarray, consider case [-2, 3, 5], including "-2" does not help in anyway to construct a subarray with minimum length, since there's no element before "-2" that we can use. Including it will only be a burden
When the queue is not empty, it can be divided into two cases again:
if the current_sum is no bigger than the absolute value of this number, it's meaningless to include anything up to this point. we should just empty the queue and start fresh. Take this example: [10,20,-30,40]. When we reach "-30", our current_sum = 30, if we include "-30", current_sum will become 0. We effetively contribute 0 value to our subarray sum with 3 elements. So we should just abandon everything till this point. Start fresh with the next element.
if the current_sum is greater than the absolute value of this number, it's meaningful to continue. Take [1,1,1,5,-1,4], you get 8 for both [1,1,1,5] and [5,-1,4], but the latter is shorter. But we don't want to just append this non-positive value into our queue, we want to group the minimum number of left neighbors of this non-positive number together that can contribute a positve value, so that when we popleft, we pop this whole group altogether. The idea behind this is that if one needs to go, everyone else in this group needs to go as well. Take this example: [10, 15, -20, ....], these three elements together contribute a +5 value, but when we shift the left boundary of the window, it's meaningless to just get ride of "10", because without "10", [15,-20] contributes a negative value, which is pointless. So if "10" is gone, [15,-20] should go with it. To implement this logic with our queue, initially we have our queue = [(10,1),(15,1)], we recursively popright, sum the popped value(15) with current value(-20), reassign to the current value(-5), increment current count(1) by the popped count(1). We do this till current value is positive. then we append this "merged" value, count pair to our queue. At the end our queue will look like this: [(5, 3)]. 5 is the combined sum of these 3 neighbor elements.
Finally, at the end of each iteration, as current_sum >= target, we continously popleft of the queue, substract popped value from current_sum, decrement current_count by the popped count, update our output if needed.

The time and space complexity is straightforward, both O(N). 
    '''
    

def max_sum(a,n):
    #code here
    cum_sum = 0
     
    for i in range(0, n):
        cum_sum += arr[i]
        
    curr_val = 0
     
    for i in range(0, n):
        curr_val += i * arr[i]
    res = curr_val
 
    for i in range(1, n):
        next_val = (curr_val - (cum_sum - arr[i-1]) + arr[i-1] * (n-1))
        curr_val = next_val
        res = max(res, next_val)
     
    return res
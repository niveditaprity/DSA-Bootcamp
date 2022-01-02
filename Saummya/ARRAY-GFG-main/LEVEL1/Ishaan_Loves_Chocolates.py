def chocolates (arr, n) : 
    #Complete the function
    
    min=arr[0]
    for i in range(n):
        if min<arr[i]:
            continue
        else:
            min=arr[i]
    return min
        

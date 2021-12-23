
def game_with_number (arr,  n) : 
    #Complete the function
    for i in range(1,n):
        arr[i-1]=arr[i-1]^arr[i]
    return arr
        

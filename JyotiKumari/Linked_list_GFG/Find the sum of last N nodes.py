def sumOfLastN_Nodes(head,n):
    #function should return sum of last n nodes
    count = 0
    curr_sum = []
    size = 0
       
    while head != None:
        size+=1
        count+=head.data
        head = head.next
        curr_sum.append(count)
       
    if size == n:
        return curr_sum[-1]
    
    return curr_sum[-1] - curr_sum[ len(curr_sum)-n-1 ]
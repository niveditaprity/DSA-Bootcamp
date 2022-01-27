#code
tc=int(input())
for i in range(tc):
    n=int(input())
    queue = ['1', '2']
    if n==1:
        print(1)
    elif n==2:
        print(2)
    else:
        if n%2==0:
            for i in range((n//2)-1):
                temp = str(queue[i])+'1'
                queue.append(temp)
                
                temp = str(queue[i])+'2'
                queue.append(temp)
        else:
            for i in range(((n-1)//2)):
                temp = str(queue[i])+'1'
                queue.append(temp)
                
                temp = str(queue[i])+'2'
                queue.append(temp)
            temp = str(queue[i])+'1'
            queue.append(temp)
        
        print(int(queue[-1]))

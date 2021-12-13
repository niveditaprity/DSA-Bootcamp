#User function Template for python3

def getMinMax( a, n):
    minimum = a[0]
    maximum = a[0]
    for i in range(n):
        if a[i] > maximum :
            maximum = a[i]
        if a[i] < minimum :
            minimum = a[i]
    return [maximum,minimum]
            
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        
        product = getMinMax(a, n)
        print(product[1], end=" ")
        print(product[0])

        T -= 1


if __name__ == "__main__":
    main()

